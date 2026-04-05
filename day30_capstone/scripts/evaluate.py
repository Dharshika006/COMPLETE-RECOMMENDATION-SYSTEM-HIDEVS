from pathlib import Path
from datetime import datetime
from data.database import SessionLocal
from data.repositories import ContentRepository, InteractionRepository
from data.models import User, Content, Interaction
from engine.orchestrator import RecommendationOrchestrator
from engine.evaluator import precision_at_k, recall_at_k, ndcg_at_k

db = SessionLocal()

content_repo = ContentRepository(db)
interaction_repo = InteractionRepository(db)

orchestrator = RecommendationOrchestrator(content_repo, interaction_repo)

user_id = 1
results = orchestrator.get_recommendations(user_id, limit=5)
recommended = [item["content_id"] for item in results]

relevant = [1, 4, 5]

precision = precision_at_k(recommended, relevant, 5)
recall = recall_at_k(recommended, relevant, 5)
ndcg = ndcg_at_k(recommended, relevant, 5)

user_count = db.query(User).count()
content_count = db.query(Content).count()
interaction_count = db.query(Interaction).count()

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

report = f"""# 📊 Auto-Generated Prototype Evaluation Report

Generated At: {timestamp}

## 📂 Live Dataset Snapshot
- Users in DB: {user_count}
- Courses in DB: {content_count}
- Interactions in DB: {interaction_count}
- Evaluated User ID: {user_id}

## 🎯 Actual Recommendation Output
Generated Recommendations: {recommended}
Seeded Relevant Items: {relevant}

## 📈 Computed Ranking Metrics
- Precision@5: {precision:.2f}
- Recall@5: {recall:.2f}
- NDCG@5: {ndcg:.2f}

## ✅ Validation Summary
- Recommendation flow executed successfully
- Metrics computed from actual orchestrator output
- Seeded interactions used for personalization
- SQLite database state captured live
- Report generated directly from evaluation script
"""

Path("evaluation_report.md").write_text(report, encoding="utf-8")
print("✅ Auto-generated evaluation report created successfully.")