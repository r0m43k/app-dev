from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route("/")
def hello():
    return "!!!"


@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/db")
def db():
    if psycopg2.connect(
        dbname = os.getenv("POSTGRES_NAME"),
        user = os.getenv("POSTGRES_USER"),
        password = os.getenv("POSTGRES_PASSWORD"),
        host = os.getenv("POSTGRES_HOST"),
        port = os.getenv("POSTGRES_PORT"),
    ):
        return {
            "database": "connected"
        }
    else:
        return {
            "database": "error"
        }        


@app.route("/info")
def info():
    return {
        "app": "d1",
        "version": "1.0",
        "environment": os.getenv("ENVIRONMENT", "development")
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)