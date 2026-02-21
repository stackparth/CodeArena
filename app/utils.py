import tempfile
import sys
import os
import subprocess
import json
from datetime import datetime

from app.database import users_col, attempts_col
from app.questions import QUESTIONS

def get_or_create_user(user_id: str):
    user = users_col.find_one({"user_id": user_id})
    if not user:
        user = {
            "user_id": user_id,
            "points": 0,
            "solved": [],
            "skipped": [],
            "created_at": datetime.utcnow()
        }
        users_col.insert_one(user)
        user = users_col.find_one({"user_id": user_id})
    return user

def safe_run_code(user_code: str, test_input: str, timeout: int = 5) -> tuple[str, bool]:
    """Execute user code safely in subprocess."""
    full_code = f"""
import sys
{user_code}

try:
    result = {test_input}
    import json
    print(json.dumps(result))
except Exception as e:
    print("__ERROR__:" + str(e))
"""
    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(full_code)
            fname = f.name
        result = subprocess.run(
            [sys.executable, fname],
            capture_output=True, text=True, timeout=timeout
        )
        os.unlink(fname)
        output = result.stdout.strip()
        if result.returncode != 0 or "__ERROR__:" in output:
            err = result.stderr.strip() or output.replace("__ERROR__:", "")
            return f"Error: {err[:200]}", False
        return output, True
    except subprocess.TimeoutExpired:
        try: os.unlink(fname)
        except: pass
        return "Error: Time Limit Exceeded (5s)", False
    except Exception as e:
        return f"Error: {str(e)}", False

def parse_expected(val):
    return json.dumps(val)
