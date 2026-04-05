# 📊 Auto-Generated Prototype Evaluation Report

Generated At: 2026-04-05 15:42:20

## 📂 Live Dataset Snapshot
- Users in DB: 10
- Courses in DB: 20
- Interactions in DB: 16
- Users Evaluated: 3

## 🎯 Actual Recommendation Output
- User 1: recs=[2, 3, 1, 6, 4], relevant=[1, 4, 5]
- User 2: recs=[1, 4, 2, 5, 3], relevant=[2, 3]
- User 3: recs=[1, 2, 3, 5, 6], relevant=[4, 8]

## 📈 Average Computed Ranking Metrics
- Precision@5: 0.27
- Recall@5: 0.56
- NDCG@5: 0.32

## ✅ Validation Summary
- Multiple users evaluated dynamically
- Metrics computed from actual orchestrator output
- Seeded interactions used as relevance labels
- SQLite DB snapshot captured live
