import requests

res = requests.post("http://127.0.0.1:8000/api/submit", json={
    "user_id": "parth",
    "question_id": 1,
    "code": "def return_100(): return 100"
})

print(res.status_code)
print(res.text)
