import os
from flask import Flask, jsonify


app = Flask(__name__)


APP_NAME = os.getenv("APP_NAME", "python-demo-app")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")


@app.route("/")
def home():
    return jsonify(
        {
            "message": "Hello from Python application!",
            "application": APP_NAME,
            "version": APP_VERSION,
            "environment": ENVIRONMENT,
        }
    )


@app.route("/health")
def health():
    return jsonify(
        {
            "status": "UP"
        }
    ), 200


@app.route("/ready")
def ready():
    return jsonify(
        {
            "status": "READY"
        }
    ), 200


@app.route("/version")
def version():
    return jsonify(
        {
            "application": APP_NAME,
            "version": APP_VERSION,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
