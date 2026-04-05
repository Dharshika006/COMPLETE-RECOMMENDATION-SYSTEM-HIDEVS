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

users = db.query(User).limit(3).all()

all_results = []
precisions = []
recalls = []
ndcgs = []

for user in users:
    results = orchestrator.get_recommendations(user.id, limit=5)
    recommended = [item["content_id"] for item in results]

    # use user's interacted content as relevance ground truth
    relevant = [
        interaction.content_id
        for interaction in db.query(Interaction)
        .filter(Interaction.user_id == user.id)
        .all()
    ]

    if not relevant:
        continue

    precision = precision_at_k(recommended, relevant, 5)
    recall = recall_at_k(recommended, relevant, 5)
    ndcg = ndcg_at_k(recommended, relevant, 5)

    precisions.append(precision)
    recalls.append(recall)
    ndcgs.append(ndcg)

    all_results.append(
        f"- User {user.id}: recs={recommended}, relevant={relevant}"
    )

avg_precision = sum(precisions) / len(precisions)
avg_recall = sum(recalls) / len(recalls)
avg_ndcg = sum(ndcgs) / len(ndcgs)

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
- Users Evaluated: {len(users)}

## 🎯 Actual Recommendation Output
{chr(10).join(all_results)}

## 📈 Average Computed Ranking Metrics
- Precision@5: {avg_precision:.2f}
- Recall@5: {avg_recall:.2f}
- NDCG@5: {avg_ndcg:.2f}

## ✅ Validation Summary
- Multiple users evaluated dynamically
- Metrics computed from actual orchestrator output
- Seeded interactions used as relevance labels
- SQLite DB snapshot captured live
"""

Path("evaluation_report.md").write_text(report, encoding="utf-8")
print("✅ Multi-user evaluation report generated successfully.")