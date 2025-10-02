from dotenv import load_dotenv
from flask import Flask, jsonify
import os

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hello World!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)