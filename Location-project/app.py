from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/location", methods=["POST"])
def location():
    data = request.get_json()

    latitude = data.get("latitude")
    longitude = data.get("longitude")
    accuracy = data.get("accuracy")

    print("\n==============================")
    print("LOCATION RECEIVED")
    print("Latitude :", latitude)
    print("Longitude:", longitude)
    print("Accuracy :", accuracy, "meters")
    print("Time     :", datetime.now().isoformat())
    print("==============================")

    return jsonify({"status": "Location received"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)