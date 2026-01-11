# 🏥 AI-Powered IoT Health Monitoring System

An end-to-end AI-driven IoT healthcare monitoring platform that collects real-time vital signs, analyzes them using deep learning and adaptive medical rules, and displays patient health status on a live web dashboard with cloud storage.

This project simulates how modern hospitals and wearable devices monitor patients remotely using Artificial Intelligence, IoT, and Cloud Computing.

---

## 🚀 Features

- 📡 Real-time IoT Sensor Simulation
  - Heart rate
  - Body temperature
  - Patient movement

- 🧠 AI-Based Health Risk Detection
  - CNN + LSTM trained on MIT-BIH ECG dataset
  - Adaptive threshold & moving-average based risk engine
  - Detects Normal, Medium Risk, and High Risk states

- ☁️ Cloud Integration
  - Firebase Firestore stores live patient records
  - Enables remote patient monitoring

- 📊 Live Web Dashboard
  - Displays vitals and AI-predicted health risk in real time
  - Updates automatically every few seconds

---

## 🏗 System Architecture

IoT Sensors (Simulated)  
        ↓  
Flask API Server  
        ↓  
AI Risk Engine (CNN + LSTM + Thresholding)  
        ↓  
Firebase Cloud Database  
        ↓  
Web Dashboard (Live Patient View)

---

## 🧠 AI Model

The deep learning model was trained using the MIT-BIH Arrhythmia ECG dataset, a globally used medical dataset for cardiac disease detection.

- Model Type: CNN + LSTM  
- Input: ECG waveform (187 samples)  
- Output: 5-class cardiac condition  
- Accuracy: ~92%

For live IoT data (heart rate, temperature, movement), an adaptive rule-based engine is used to determine health risk, simulating how ICU monitors work in real hospitals.

---

## 🛠 Technologies Used

| Category | Tools |
|--------|------|
| Programming | Python |
| Web Server | Flask |
| AI / ML | TensorFlow, CNN, LSTM |
| Cloud | Firebase Firestore |
| Frontend | HTML, JavaScript |
| Data Processing | NumPy, Pandas |
| Deployment | GitHub |

---

## ▶️ How to Run the Project

### 1. Install dependencies

pip install flask firebase-admin tensorflow numpy pandas

---

### 2. Add Firebase Key
Place your Firebase Admin SDK key in the project folder as:

firebase_key.json

(This file is not included for security reasons.)

---

### 3. Start the server

python server.py

---

### 4. Start the IoT sensor

Open another terminal:

python sensor_simulator.py

---

### 5. Open dashboard

Open in browser:

http://127.0.0.1:5000

You will see a live AI-powered health monitoring dashboard.

---

## 📂 Project Structure

IoT_Health_Project/  
│  
├── server.py  
├── ai_predictor.py  
├── sensor_simulator.py  
├── firebase_key.json   (not in GitHub)  
├── health_data.csv    (not in GitHub)  
│  
├── templates/  
│   └── dashboard.html  
│  
└── static/

---

## 🧪 Example Output

Heart Rate | Temperature | Movement | AI Risk  
78 | 36.8°C | 1 | Normal  
105 | 38.5°C | 2 | Medium  
132 | 39.2°C | 2 | High Risk  

---

## 🧾 Resume-Ready Description

Developed an AI-powered IoT Health Monitoring System using Python, Flask, Firebase, and deep learning. Implemented CNN and LSTM models trained on MIT-BIH ECG data achieving ~92% accuracy for cardiac anomaly detection. Built a real-time sensor pipeline, cloud-based patient database, and live monitoring dashboard for remote healthcare applications.

---

## 👨‍⚕️ Use Cases

- Remote patient monitoring  
- ICU vital tracking  
- Wearable health devices  
- Telemedicine platforms  

---

## ⭐ Author

Gopal Niranjan  
AI | IoT | Cloud | Healthcare Systems
