# 📊 Auto-Generated Prototype Evaluation Report

Generated At: 2026-04-05 16:08:55

## 📂 Live Dataset Snapshot
- Users in DB: 10
- Courses in DB: 20
- Interactions in DB: 16
- Users Evaluated: 10

## 🎯 Actual Recommendation Output
- User 1: recs=[2, 3, 1, 6, 4], relevant=[1, 4, 5]
- User 2: recs=[1, 4, 2, 5, 3], relevant=[2, 3]
- User 3: recs=[1, 2, 3, 5, 6], relevant=[4, 8]
- User 4: recs=[3, 1, 4, 2, 5], relevant=[1, 2]
- User 5: recs=[1, 2, 4, 5, 3], relevant=[3, 7]
- User 6: recs=[1, 2, 3, 4, 5], relevant=[6]
- User 7: recs=[1, 2, 3, 4, 5], relevant=[9]
- User 8: recs=[1, 2, 3, 4, 5], relevant=[12]
- User 9: recs=[1, 2, 3, 4, 5], relevant=[15]
- User 10: recs=[1, 2, 3, 4, 5], relevant=[18]

## 📈 Average Computed Ranking Metrics
- Precision@5: 0.14
- Recall@5: 0.32
- NDCG@5: 0.18

## ✅ Validation Summary
- Multiple users evaluated dynamically
- Metrics computed from actual orchestrator output
- Seeded interactions used as relevance labels
- SQLite DB snapshot captured live
