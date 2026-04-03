from engine.candidate_gen import CandidateGenerator
from engine.scorer import RecommendationScorer

class RecommendationOrchestrator:
    def __init__(self, content_repo, interaction_repo):
        self.content_repo = content_repo
        self.interaction_repo = interaction_repo
        self.generator = CandidateGenerator()
        self.scorer = RecommendationScorer()
        self.cache = {}

    def get_recommendations(self, user_id, limit=5):
        if user_id in self.cache:
            return self.cache[user_id]

        history = self.interaction_repo.get_user_history(user_id)
        all_content = self.content_repo.get_all()

        if not history:
            recommendations = sorted(
                all_content,
                key=lambda x: x.popularity,
                reverse=True
            )[:limit]
        else:
            candidates = []
            candidates += self.generator.generate_from_history(history, all_content)
            candidates += self.generator.generate_by_category(history, all_content)
            candidates += self.generator.generate_trending(all_content)

            unique = {c.id: c for c in candidates}
            ranked = self.scorer.score(list(unique.values()), history)
            recommendations = ranked[:limit]

        result = [
            {
                "content_id": c.id,
                "title": c.title,
                "explanation": f"Popular in {c.category}"
            }
            for c in recommendations
        ]

        self.cache[user_id] = result
        return result