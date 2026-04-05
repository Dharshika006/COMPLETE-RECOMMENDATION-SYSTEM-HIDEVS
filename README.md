# 🚀 Complete Recommendation System Prototype

A **functional recommendation system prototype** built with **FastAPI, SQLite, SQLAlchemy, and a modular recommendation engine**.

This project demonstrates backend system design for personalized course recommendations using API routing, SQLite persistence, modular ranking logic, cold-start fallback, feedback collection, and seeded sample-data evaluation.

It is intentionally positioned as a **portfolio-grade backend prototype** focused on clean architecture and reproducible behavior using seeded data.

---

# 📌 Project Overview
This system provides **personalized course recommendations** using multiple ranking strategies over a seeded sample dataset.

### ✨ Implemented Features
- Personalized recommendations based on seeded user history
- Category similarity recommendations
- Popularity-based fallback for cold-start users
- SQLite database with normalized schema
- REST API built using FastAPI
- Dashboard homepage for API navigation
- Feedback recording endpoint
- Seeded sample dataset for reproducible testing
- Basic unit tests for API, engine, and data layer
- Prototype evaluation on sample seeded relevance data

---

# 🏗️ System Architecture
```text
User Request
   ↓
FastAPI Endpoint
   ↓
Recommendation Orchestrator
   ↓
Candidate Generator
   ↓
Scorer + Similarity Engine
   ↓
SQLite Database
   ↓
JSON Response + Dashboard
```

---

# 📁 Project Structure
```text
day30_capstone/
├── api/
│   └── app.py
├── data/
│   ├── database.py
│   ├── models.py
│   └── repositories.py
├── engine/
│   ├── orchestrator.py
│   ├── candidate_gen.py
│   ├── scorer.py
│   ├── similarity.py
│   └── evaluator.py
├── scripts/
│   ├── seed_data.py
│   └── evaluate.py
├── tests/
│   ├── test_api.py
│   ├── test_data.py
│   └── test_engine.py
├── screenshots/
├── evaluation_report.md
├── recommendation.db
└── README.md
```

---

# ⚙️ Setup Instructions

## 1) Clone the Repository
```bash
git clone <your-repo-link>
cd day30_capstone
```

## 2) Install Dependencies
```bash
pip install -r requirements.txt
```

## 3) Seed Sample Data
```bash
python -m scripts.seed_data
```

## 4) Start API Server
```bash
uvicorn api.app:app --reload
```

Open in browser:
```text
http://127.0.0.1:8000/
```

Swagger docs:
```text
http://127.0.0.1:8000/docs
```

---

# 📘 API Documentation

## ✅ Health Check
```http
GET /health
```

### Response
```json
{
  "status": "healthy"
}
```

---

## 🎯 Get Recommendations
```http
GET /recommend/{user_id}
```

### Example
```http
GET /recommend/1
```

### Response
```json
[
  {
    "content_id": 1,
    "title": "Course 1",
    "explanation": "Recommended from seeded interaction patterns"
  }
]
```

---

## ⭐ Record Feedback
```http
POST /feedback
```

### Request
```json
{
  "user_id": 1,
  "content_id": 4,
  "rating": 5
}
```

### Response
```json
{
  "message": "Feedback recorded successfully"
}
```

---

## 📊 Metrics
```http
GET /metrics
```

This endpoint provides **basic prototype-level request statistics and service health details**.

---

# 🗄️ Database Schema Diagram
```text
users
 ├── id (PK)
 ├── name
 ├── interests
 └── created_at

content
 ├── id (PK)
 ├── title
 ├── category
 ├── difficulty
 └── popularity

interactions
 ├── user_id (FK → users.id)
 ├── content_id (FK → content.id)
 ├── type
 ├── rating
 └── created_at
```

---

# 🧠 Recommendation Strategies
The engine combines 3 prototype strategies:

1. **History-Based Filtering**
2. **Category Similarity**
3. **Popularity Fallback**

This ensures:
- personalization
- cold-start handling
- deterministic seeded behavior

---

# 📊 Auto-Generated Evaluation Pipeline
Generated using:

```bash
python -m scripts.evaluate
```

The evaluation computes:
- Precision@5
- Recall@5
- NDCG@5

using **actual recommendation outputs over seeded sample relevance sets**.

See full details in:

```text
evaluation_report.md
```

---

# 🧪 Running Tests
Run the available basic unit tests:

```bash
pytest
```

These validate:
- API endpoint behavior
- evaluator metric functions
- database seeded row presence
- recommendation fallback flow

---

# 🎥 Project Demo Video
Demo video (under 3 minutes):

https://youtu.be/nzMbw3j8UH8?feature=shared

---

# 🏗️ Architecture Decisions
- **FastAPI** used for simple REST API routing
- **SQLite** used for lightweight local persistence
- **Repository pattern** used for clean data abstraction
- **Modular engine design** used for easy experimentation
- **Separate evaluation pipeline** used for reproducible prototype metrics
- **Dashboard layer** added for easier demonstration

---

# 📌 Scope and Future Improvements
Current scope:
- prototype recommendation workflow
- seeded sample-data validation
- backend API demonstration

Possible future improvements:
- Redis caching
- JWT authentication
- real-user datasets
- frontend React dashboard
- Docker deployment
- cloud deployment

---

Built as part of **Day 30 Capstone: Complete Recommendation System Prototype**