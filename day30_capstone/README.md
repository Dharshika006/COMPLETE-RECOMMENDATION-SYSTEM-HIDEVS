# 🚀 Complete Recommendation System Microservice

A production-ready recommendation system built with **FastAPI, SQLite, SQLAlchemy, and a modular recommendation engine**.  
This project combines database design, ranking logic, REST API development, performance evaluation, and dashboard monitoring into a portfolio-grade microservice.

---

# 📌 Project Overview
This system provides **personalized course recommendations** using multiple ranking strategies.

### ✨ Key Features
- Personalized recommendations based on user history
- Category similarity recommendations
- Trending/popularity fallback
- Cold-start support for new users
- SQLite database with normalized schema
- REST API with FastAPI
- Request tracing and metrics
- Dashboard homepage
- Load testing with 10 concurrent users
- Auto-generated evaluation report
- Unit tests for API and engine

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
│   ├── evaluate.py
│   └── load_test.py
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
    "explanation": "Popular in AI"
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

# 🧠 Recommendation Strategies
The engine combines 3 strategies:

1. **History-Based Filtering**
2. **Category Similarity**
3. **Popularity/Trending Ranking**

This ensures:
- personalization
- novelty
- cold-start robustness

---

# 📊 Performance Report Summary
Generated automatically using:
```bash
python -m scripts.evaluate
```

### Results
- Precision@5: 0.60
- Recall@5: 0.75
- NDCG@5: 0.82
- Average Response Time: 42 ms
- Concurrent Users Tested: 10

See full details in:
```text
evaluation_report.md
```

---

# 🧪 Running Tests
```bash
pytest
```

---

# 🎥 Project Demo Video
Demo video (under 3 minutes):



# 🏗️ Architecture Decisions
- **FastAPI** chosen for high-performance REST APIs
- **SQLite** used for lightweight local persistence
- **Repository pattern** for clean database abstraction
- **Modular engine design** for scalability
- **Separate evaluation pipeline** for reproducible reporting
- **Dashboard enhancement** for easier demo and usability

---

# 📌 Future Improvements
- Redis caching
- JWT authentication
- Real-time personalization
- Frontend React dashboard
- Docker deployment
- Cloud hosting on Render

---

Built as part of **Day 30 Capstone: Complete Recommendation System**.
