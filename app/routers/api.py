import random
from datetime import datetime
from fastapi import APIRouter, HTTPException

from app.questions import QUESTIONS
from app.models import SubmitRequest, SkipRequest, UserRegister, UserLogin
from app.database import users_col, attempts_col, get_rank, RANKS
from app.utils import get_or_create_user, safe_run_code, parse_expected
from app.auth import verify_password, get_password_hash, create_access_token
router = APIRouter(prefix="/api")

@router.post("/register")
def register(user: UserRegister):
    existing = users_col.find_one({"username": user.username})
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    users_col.insert_one({
        "username": user.username,
        "user_id": user.username,
        "password_hash": get_password_hash(user.password),
        "points": 0,
        "solved": [],
        "skipped": [],
        "created_at": datetime.utcnow()
    })
    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: UserLogin):
    db_user = users_col.find_one({"username": user.username})
    if not db_user or not verify_password(user.password, db_user.get("password_hash", "")):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    
    access_token = create_access_token(data={"sub": db_user["username"]})
    return {"access_token": access_token, "token_type": "bearer", "user_id": db_user["username"]}

@router.get("/random-question")
def get_random_question(difficulty: str | None = None, exclude: str = ""):
    excluded = [int(x) for x in exclude.split(",") if x.strip().isdigit()]
    pool = QUESTIONS
    if difficulty:
        pool = [q for q in pool if q["difficulty"] == difficulty]
    pool = [q for q in pool if q["id"] not in excluded]
    if not pool:
        pool = QUESTIONS  # fallback
    q = random.choice(pool)
    return {
        "id": q["id"], "title": q["title"], "difficulty": q["difficulty"],
        "points": q["points"], "description": q["description"],
        "starter": q["starter"], "hint": q["hint"], "tags": q["tags"],
        "total_tests": len(q["tests"])
    }

@router.get("/question/{qid}")
def get_question(qid: int):
    q = next((q for q in QUESTIONS if q["id"] == qid), None)
    if not q:
        raise HTTPException(status_code=404, detail="Question not found")
    return {
        "id": q["id"], "title": q["title"], "difficulty": q["difficulty"],
        "points": q["points"], "description": q["description"],
        "starter": q["starter"], "hint": q["hint"], "tags": q["tags"],
        "total_tests": len(q["tests"])
    }

@router.get("/questions")
def list_questions():
    return [{"id": q["id"], "title": q["title"], "difficulty": q["difficulty"],
             "points": q["points"], "tags": q["tags"]} for q in QUESTIONS]

@router.get("/user/{user_id}")
def get_user(user_id: str):
    user = get_or_create_user(user_id)
    rank = get_rank(user["points"])
    next_rank = None
    for r in RANKS:
        if r["min"] > user["points"]:
            next_rank = r
            break
    return {
        "user_id": user_id,
        "points": user["points"],
        "solved": user["solved"],
        "skipped": user["skipped"],
        "rank": rank,
        "next_rank": next_rank,
    }

@router.post("/submit")
def submit_code(req: SubmitRequest):
    q = next((q for q in QUESTIONS if q["id"] == req.question_id), None)
    if not q:
        raise HTTPException(status_code=404, detail="Question not found")

    results = []
    all_passed = True
    for i, tc in enumerate(q["tests"]):
        output, ok = safe_run_code(req.code, tc["input"])
        expected_str = parse_expected(tc["expected"])
        passed = ok and output.strip() == expected_str.strip()
        if not passed:
            all_passed = False
        results.append({
            "case": i + 1,
            "input": tc["input"],
            "expected": expected_str,
            "got": output,
            "passed": passed,
        })

    user = get_or_create_user(req.user_id)
    already_solved = req.question_id in user.get("solved", [])
    points_earned = 0

    if all_passed and not already_solved:
        points_earned = q["points"]
        users_col.update_one(
            {"user_id": req.user_id},
            {"$inc": {"points": points_earned},
             "$addToSet": {"solved": req.question_id},
             "$pull": {"skipped": req.question_id}}
        )

    # Save attempt
    attempts_col.insert_one({
        "user_id": req.user_id,
        "question_id": req.question_id,
        "code": req.code,
        "all_passed": all_passed,
        "results": results,
        "points_earned": points_earned,
        "attempted_at": datetime.utcnow()
    })

    updated_user = get_or_create_user(req.user_id)
    return {
        "all_passed": all_passed,
        "results": results,
        "points_earned": points_earned,
        "total_points": updated_user["points"],
        "rank": get_rank(updated_user["points"])
    }

@router.post("/skip")
def skip_question(req: SkipRequest):
    get_or_create_user(req.user_id)
    users_col.update_one(
        {"user_id": req.user_id},
        {"$addToSet": {"skipped": req.question_id}}
    )
    return {"success": True}

@router.get("/history/{user_id}")
def get_history(user_id: str):
    attempts = list(attempts_col.find(
        {"user_id": user_id},
        {"_id": 0}
    ).sort("attempted_at", -1).limit(50))
    for a in attempts:
        q = next((q for q in QUESTIONS if q["id"] == a["question_id"]), None)
        if q:
            a["question_title"] = q["title"]
            a["difficulty"] = q["difficulty"]
        a["attempted_at"] = a["attempted_at"].isoformat() if hasattr(a.get("attempted_at"), "isoformat") else str(a.get("attempted_at", ""))
    return attempts

@router.get("/ranks")
def get_ranks():
    return RANKS

@router.get("/leaderboard")
def get_leaderboard():
    users = list(users_col.find(
        {},
        {"_id": 0, "username": 1, "points": 1}
    ).sort("points", -1).limit(100))
    for u in users:
        u["rank"] = get_rank(u["points"])
    return users
