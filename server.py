from flask import Flask, request, jsonify, render_template
import csv
import os
from ai_predictor import predict_risk

# Firebase
import firebase_admin
from firebase_admin import credentials, firestore

# -------------------- Firebase Init --------------------
cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# -------------------- Flask Init --------------------
app = Flask(__name__)

FILE = "health_data.csv"

# Create CSV file if not exists
if not os.path.exists(FILE):
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["heart_rate", "temperature", "movement", "risk"])

# -------------------- Dashboard --------------------
@app.route("/")
def dashboard():
    return render_template("dashboard.html")

# -------------------- Receive IoT Data --------------------
@app.route("/data", methods=["POST"])
def receive_data():
    data = request.json

    heart_rate = int(data["heart_rate"])
    temperature = float(data["temperature"])
    movement = int(data["movement"])

    # AI Prediction
    risk = int(predict_risk(heart_rate, temperature, movement))

    # Save to CSV
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([heart_rate, temperature, movement, risk])

    # Save to Firebase Cloud
    db.collection("patients").add({
        "heart_rate": heart_rate,
        "temperature": temperature,
        "movement": movement,
        "risk": risk
    })

    return jsonify({"status": "saved", "risk": risk})

# -------------------- Show All Data --------------------
@app.route("/all")
def all():
    rows = []
    with open(FILE) as f:
        next(f)
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 4:
                hr, temp, move, risk = parts
                rows.append({
                    "heart_rate": hr,
                    "temperature": temp,
                    "movement": move,
                    "risk": risk
                })
    return jsonify(rows)

# -------------------- Run Server --------------------
if __name__ == "__main__":
    app.run(debug=True)
