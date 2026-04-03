from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uuid
import time

from data.database import SessionLocal, engine, Base
from data.repositories import (
    UserRepository,
    ContentRepository,
    InteractionRepository
)
from engine.orchestrator import RecommendationOrchestrator

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Complete Recommendation System",
    description="Production-ready recommendation microservice",
    version="1.0.0"
)

# Track simple system metrics
metrics_store = {
    "total_requests": 0,
    "recommend_requests": 0,
    "avg_response_time_ms": 0
}


class FeedbackRequest(BaseModel):
    user_id: int
    content_id: int
    rating: float


# -----------------------------
# Middleware for request tracing
# -----------------------------
@app.middleware("http")
async def add_request_id(request: Request, call_next):
    start = time.time()

    request.state.request_id = str(uuid.uuid4())
    metrics_store["total_requests"] += 1

    response = await call_next(request)

    elapsed = (time.time() - start) * 1000
    metrics_store["avg_response_time_ms"] = round(elapsed, 2)

    response.headers["X-Request-ID"] = request.state.request_id
    return response


# -----------------------------
# Dashboard Home Page
# -----------------------------
@app.get("/", response_class=HTMLResponse)
def home():
    return f"""
    <html>
        <head>
            <title>Recommendation Dashboard</title>
        </head>
        <body style="font-family: Arial; padding: 30px;">
            <h1>🚀 Recommendation System Dashboard</h1>
            <p><b>Status:</b> Running Successfully</p>

            <h2>📊 Quick Metrics</h2>
            <ul>
                <li>Total Requests: {metrics_store["total_requests"]}</li>
                <li>Recommendation Requests: {metrics_store["recommend_requests"]}</li>
                <li>Avg Response Time: {metrics_store["avg_response_time_ms"]} ms</li>
            </ul>

            <h2>🔗 Available Endpoints</h2>
            <ul>
                <li><a href="/health">Health Check</a></li>
                <li><a href="/recommend/1">Recommendations for User 1</a></li>
                <li><a href="/metrics">Metrics</a></li>
                <li><a href="/docs">Swagger API Docs</a></li>
            </ul>
        </body>
    </html>
    """


# -----------------------------
# Health Check
# -----------------------------
@app.get("/health")
def health():
    return {"status": "healthy"}


# -----------------------------
# Get Recommendations
# -----------------------------
@app.get("/recommend/{user_id}")
def recommend(user_id: int):
    db = SessionLocal()

    user_repo = UserRepository(db)
    content_repo = ContentRepository(db)
    interaction_repo = InteractionRepository(db)

    user = user_repo.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    metrics_store["recommend_requests"] += 1

    engine_obj = RecommendationOrchestrator(
        content_repo,
        interaction_repo
    )

    return engine_obj.get_recommendations(user_id)


# -----------------------------
# Record Feedback
# -----------------------------
@app.post("/feedback")
def feedback(req: FeedbackRequest):
    db = SessionLocal()
    interaction_repo = InteractionRepository(db)

    interaction_repo.record_feedback(
        req.user_id,
        req.content_id,
        req.rating
    )

    return {
        "message": "Feedback recorded successfully",
        "user_id": req.user_id,
        "content_id": req.content_id
    }


# -----------------------------
# Metrics Endpoint
# -----------------------------
@app.get("/metrics")
def metrics():
    return metrics_store