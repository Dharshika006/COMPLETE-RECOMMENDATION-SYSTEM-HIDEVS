class RecommendationScorer:
    def score(self, candidates, history):
        history_ids = {h.content_id for h in history}
        scored = []

        for content in candidates:
            score = content.popularity

            if content.id not in history_ids:
                score += 2

            scored.append((content, score))

        scored.sort(key=lambda x: x[1], reverse=True)
        return [item[0] for item in scored]