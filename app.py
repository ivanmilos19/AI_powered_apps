from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
port = int(os.getenv("PORT"))

@app.route("/")
def home():
    return os.getenv("OPENAI_API_KEY", "No API key found")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)