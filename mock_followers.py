from flask import Flask, jsonify
import random
from datetime import datetime

app = Flask(__name__)

@app.route("/followers/<username>")
def followers(username):
    count = random.choice([1000, 5000, 10000, 50000, 1000000])
    data = {
        "username": username,
        "follower_count": count,
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "source": "Mock API - Educational Testing Only"
    }
    return jsonify(data)

@app.route("/")
def home():
    return "✅ Mock Follower API Running (Educational Only)"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    