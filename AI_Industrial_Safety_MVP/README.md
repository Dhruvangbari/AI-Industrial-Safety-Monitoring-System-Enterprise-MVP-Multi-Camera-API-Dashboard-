# AI Industrial Safety MVP
# 🏭 AI Industrial Safety Monitoring System – Enterprise MVP

An enterprise-ready AI-based Industrial Safety Monitoring System designed for real-world deployment scenarios.

This system performs real-time safety compliance detection using computer vision and provides:

- Multi-camera monitoring
- Helmet & face mask detection
- Violation logging with cooldown control
- Evidence image storage
- REST API backend
- Real-time dashboard analytics

Built for:
- Smart factories
- Construction sites
- Industrial compliance automation
- Startup MVP development
- AI product prototyping

---

## 🚀 Core Features

### 🎥 Multi-Camera Support
Monitor multiple camera feeds simultaneously (Webcam / RTSP supported).

### 🦺 Safety Compliance Detection
Detects:
- Person
- Safety Helmet
- Face Mask

Automatically evaluates compliance and flags violations.

### 🧠 Intelligent Violation Control
- Cooldown system to prevent duplicate logs
- Structured CSV logging
- Image evidence storage

### 🌐 REST API Backend
FastAPI-powered API for:
- Retrieving violation data
- Integration with external systems
- Cloud-ready architecture

### 📊 Live Dashboard
Streamlit-based analytics dashboard for:
- Viewing violations
- Basic trend visualization
- Data inspection

---

## 🏗 System Architecture

1. Video Stream → YOLOv8 Detection
2. Object Tracking Layer
3. Compliance Evaluation Engine
4. Violation Logging Module
5. API Layer (FastAPI)
6. Dashboard Interface (Streamlit)

Modular design enables easy scalability and future upgrades.

---

## 📂 Project Structure

AI_Industrial_Safety_MVP/
│
├── app/
│   ├── main.py
│   ├── detector.py
│   ├── tracker.py
│   ├── compliance.py
│   ├── logger.py
│   ├── config.py
│   └── api.py
│
├── dashboard/
│   └── dashboard.py
│
├── logs/
│   ├── violations.csv
│   └── images/
│
├── requirements.txt
└── README.md

---

## 🛠 Tech Stack

- Python 3.10+
- Ultralytics YOLOv8
- OpenCV
- PyTorch
- FastAPI
- Streamlit
- Pandas

---

## ⚙️ Installation

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt

Enterprise-level Industrial Safety Monitoring System with:
- Multi-camera support
- Helmet & Mask compliance logic
- Violation logging
- REST API backend (FastAPI)
- Streamlit dashboard

Run main engine:
python app/main.py

Run API:
uvicorn app.api:app --reload

Run dashboard:
streamlit run dashboard/dashboard.py
