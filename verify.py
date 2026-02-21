import urllib.request
try:
    with urllib.request.urlopen('http://127.0.0.1:8000/api/ranks') as response:
        print(response.read().decode())
except Exception as e:
    print("Error 127.0.0.1:", e)
try:
    with urllib.request.urlopen('http://localhost:8000/api/ranks') as response:
        print(response.read().decode())
except Exception as e:
    print("Error localhost:", e)
