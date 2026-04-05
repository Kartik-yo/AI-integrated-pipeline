from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "ok", "message": "AI Pipeline v1"}

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

`app/requirements.txt`:
```
flask==3.0.0
pytest==7.4.0