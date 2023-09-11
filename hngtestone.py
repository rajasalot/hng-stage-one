from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import random

app = Flask(__name__)

format = "%Y-%m-%dT%H:%M:%SZ"

@app.route("/api")
def slack_user():
    user_data = {
        "slack_name": request.args.get("slack_name"),
        "current_day": datetime.now().strftime('%A'),
        "utc_time": get_current_utc_time().strftime(format),
        "track": request.args.get("track"),
        "github_file_url": "https://github.com/rajasalot/hng-stage-one/blob/main/hngtestone.py",
        "github_repo_url": "https://github.com/rajasalot/hng-stage-one",
        "status_code": 200
    }
    return jsonify(user_data), 200

def get_current_utc_time():
    current_time = datetime.utcnow()
    # Add or subtract a random number of seconds within +/-2 minutes (120 seconds)
    random_seconds = random.randint(-120, 120)
    adjusted_time = current_time + timedelta(seconds=random_seconds)
    
    return adjusted_time

if __name__ == "__main__":
    app.run(debug=True)
