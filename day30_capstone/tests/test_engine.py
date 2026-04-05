from data.database import SessionLocal
from data.repositories import ContentRepository, InteractionRepository
from engine.orchestrator import RecommendationOrchestrator


def test_recommendation_returns_results():
    db = SessionLocal()

    content_repo = ContentRepository(db)
    interaction_repo = InteractionRepository(db)

    orchestrator = RecommendationOrchestrator(
        content_repo,
        interaction_repo
    )

    results = orchestrator.get_recommendations(1, limit=5)

    assert isinstance(results, list)
    assert len(results) > 0
    assert "content_id" in results[0]


def test_cold_start_user_returns_results():
    db = SessionLocal()

    content_repo = ContentRepository(db)
    interaction_repo = InteractionRepository(db)

    orchestrator = RecommendationOrchestrator(
        content_repo,
        interaction_repo
    )

    # user 999 does not exist → cold-start fallback
    results = orchestrator.get_recommendations(999, limit=5)

    assert isinstance(results, list)
    assert len(results) > 0