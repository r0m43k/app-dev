from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "!!!"


@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/info")
def info():
    return {
        "app": "dev-1",
        "version": "0.0.1",
        "environment": os.getenv("ENVIRONMENT", "development")
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)