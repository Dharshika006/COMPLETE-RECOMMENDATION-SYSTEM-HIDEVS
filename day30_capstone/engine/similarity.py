class SimilarityEngine:
    def category_similarity(self, item1, item2):
        return 1.0 if item1.category == item2.category else 0.0

    def difficulty_similarity(self, item1, item2):
        return 1.0 if item1.difficulty == item2.difficulty else 0.5

    def combined_similarity(self, item1, item2):
        return (
            self.category_similarity(item1, item2) * 0.7
            + self.difficulty_similarity(item1, item2) * 0.3
        )