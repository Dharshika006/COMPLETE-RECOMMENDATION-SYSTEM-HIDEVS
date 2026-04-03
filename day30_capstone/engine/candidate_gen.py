class CandidateGenerator:
    def generate_from_history(self, history, all_content):
        seen = {h.content_id for h in history}
        return [c for c in all_content if c.id not in seen]

    def generate_by_category(self, history, all_content):
        if not history:
            return []

        liked_categories = set()
        for h in history:
            for c in all_content:
                if c.id == h.content_id:
                    liked_categories.add(c.category)

        return [c for c in all_content if c.category in liked_categories]

    def generate_trending(self, all_content):
        return sorted(all_content, key=lambda x: x.popularity, reverse=True)