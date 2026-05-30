# AI Clinical Assistant

> A full-stack AI-powered healthcare management platform combining Machine Learning, Generative AI, and Speech AI to streamline patient care and clinical workflows.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [System Architecture](#system-architecture)
- [Project Structure](#project-structure)
- [Database Schema](#database-schema)
- [Getting Started](#getting-started)
- [Running the Application](#running-the-application)
- [Future Roadmap](#future-roadmap)
- [Author](#author)

---

## Overview

AI Clinical Assistant is a healthcare management platform built for both patients and healthcare professionals. It automates risk prediction, generates AI-powered medical summaries, transcribes doctor consultations using voice AI, and provides comprehensive dashboards for patient monitoring — all within a single integrated system.

---

## Features

### Patient Dashboard
- Health information intake form
- Heart disease risk prediction powered by XGBoost
- BMI analysis with automatic health status classification
- AI-generated medical summaries via Mistral AI
- Downloadable PDF medical report generation
- Persistent patient record storage

### Doctor Dashboard
- Real-time patient monitoring system
- Patient record search and history viewing
- Consultation note creation and management
- Full consultation history tracking
- Voice-based consultation transcription using Whisper AI
- High-risk patient flagging and monitoring

### AI Capabilities
| Feature | Model |
|---|---|
| Heart Disease Risk Prediction | XGBoost |
| Medical Summary Generation | Mistral AI |
| Consultation Transcription | OpenAI Whisper |

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI, Python |
| Frontend | Streamlit |
| Database | SQLite, SQLAlchemy ORM |
| Machine Learning | XGBoost, Scikit-learn, NumPy, Pandas |
| Generative AI | Mistral AI |
| Speech AI | OpenAI Whisper |

---

## System Architecture

```
Patient Dashboard
        │
        ▼
Patient Health Data Entry
        │
        ▼
XGBoost Prediction Engine ──────► Heart Risk Assessment
        │
        ▼
Mistral AI ──────────────────────► Medical Summary Generation
        │
        ▼
BMI Analysis Engine
        │
        ▼
SQLite Database (via SQLAlchemy)
        │
        ▼
PDF Report Generation
        │
        ▼
Doctor Dashboard
   ├── Patient Search & Monitoring
   ├── Consultation Notes
   └── Whisper AI Transcription
```

---

## Project Structure

```
AI-Clinical-Assistant/
│
├── backend/
│   ├── routes/            # API route handlers
│   ├── services/          # Business logic layer
│   ├── database/          # DB connection and session management
│   ├── models/            # SQLAlchemy ORM models
│   ├── rag_data/          # Data for future RAG integration
│   └── main.py            # FastAPI application entry point
│
├── frontend/
│   ├── patient_dashboard.py   # Patient-facing Streamlit UI
│   └── doctor_dashboard.py    # Doctor-facing Streamlit UI
│
├── screenshots/           # Application screenshots
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Database Schema

### `patients`

| Column | Type | Description |
|---|---|---|
| `patient_id` | INTEGER | Primary key |
| `name` | TEXT | Patient full name |
| `age` | INTEGER | Patient age |
| `symptoms` | TEXT | Reported symptoms |
| `prediction` | TEXT | Risk prediction result |
| `ai_summary` | TEXT | AI-generated medical summary |

### `consultation_notes`

| Column | Type | Description |
|---|---|---|
| `note_id` | INTEGER | Primary key |
| `patient_id` | INTEGER | Foreign key to patients |
| `consultation_notes` | TEXT | Doctor's consultation notes |
| `timestamp` | DATETIME | Date and time of consultation |

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/AI-Clinical-Assistant.git
cd AI-Clinical-Assistant
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

---

## Running the Application

### Start the Backend

```bash
cd backend
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`  
Interactive API docs: `http://127.0.0.1:8000/docs`

### Start the Patient Dashboard

```bash
cd frontend
streamlit run patient_dashboard.py
```

### Start the Doctor Dashboard

```bash
cd frontend
streamlit run doctor_dashboard.py
```

---

## Future Roadmap

### RAG Medical Assistant
- Medical PDF knowledge base integration
- Vector search using FAISS
- Context-aware healthcare chatbot powered by LangChain

### Authentication & Access Control
- Role-based login (Doctor / Patient)
- Secure session management

### Deployment
- Docker containerization
- Cloud deployment via Render

---

## Author

**Sumit Shivaji Ghugare**  
AI/ML Enthusiast · Data Analyst · Python Developer

---

*If you found this project useful, consider giving it a ⭐ on GitHub.*
