import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

username = os.environ.get("MONGO_USERNAME")
password = os.environ.get("MONGO_PASSWORD")
cluster = os.environ.get("MONGO_CLUSTER", "cluster0.ejap6tl.mongodb.net")
app_name = os.environ.get("MONGO_APP_NAME", "Cluster0")

uri = f"mongodb+srv://{username}:{password}@{cluster}/?appName={app_name}"
client = MongoClient(uri)

db = client["codearena"]
users_col = db["users"]
attempts_col = db["attempts"]

RANKS = [
    {"name": "Code Newbie",          "icon": "🧒", "min": 0,      "max": 499,    "tier": "Beginner"},
    {"name": "Syntax Starter",       "icon": "🧑", "min": 500,    "max": 1499,   "tier": "Beginner"},
    {"name": "Bug Hunter",           "icon": "🔧", "min": 1500,   "max": 2999,   "tier": "Beginner"},
    {"name": "Logic Learner",        "icon": "⚡", "min": 3000,   "max": 4999,   "tier": "Beginner"},
    {"name": "Algorithm Apprentice", "icon": "🚀", "min": 5000,   "max": 7999,   "tier": "Intermediate"},
    {"name": "Problem Solver",       "icon": "🧠", "min": 8000,   "max": 11999,  "tier": "Intermediate"},
    {"name": "Code Warrior",         "icon": "🔥", "min": 12000,  "max": 16999,  "tier": "Intermediate"},
    {"name": "Debug Knight",         "icon": "🛡️", "min": 17000,  "max": 22999,  "tier": "Intermediate"},
    {"name": "Algorithm Gladiator",  "icon": "⚔️", "min": 23000,  "max": 29999,  "tier": "Advanced"},
    {"name": "Code Master",          "icon": "👑", "min": 30000,  "max": 39999,  "tier": "Advanced"},
    {"name": "System Architect",     "icon": "🔭", "min": 40000,  "max": 54999,  "tier": "Advanced"},
    {"name": "Grand Coder",          "icon": "💀", "min": 55000,  "max": 74999,  "tier": "Advanced"},
    {"name": "Legendary Hacker",     "icon": "💠", "min": 75000,  "max": 99999,  "tier": "Elite"},
    {"name": "Mr. Robot",            "icon": "🤖", "min": 100000, "max": 999999999, "tier": "Elite"},
]

def get_rank(pts: int):
    for r in RANKS:
        if r["min"] <= pts <= r["max"]:
            return r
    return RANKS[0]
