import urllib.request
import json
data = json.dumps({"user_id": "parth", "question_id": 1, "code": "def return_100(): return 100"}).encode()
req = urllib.request.Request('http://127.0.0.1:8000/api/submit', data=data, headers={'Content-Type': 'application/json'})
try:
    with urllib.request.urlopen(req) as response:
        print("Status:", response.status)
        print("Body:", response.read().decode())
except Exception as e:
    import urllib.error
    if isinstance(e, urllib.error.HTTPError):
        print("HTTP ERROR:", e.code)
        print("ERROR BODY:", e.read().decode())
    else:
        print("OTHER ERROR:", e)
