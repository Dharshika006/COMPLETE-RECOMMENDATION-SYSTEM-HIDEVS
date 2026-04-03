import math

def precision_at_k(recommended, relevant, k=5):
    recommended = recommended[:k]
    hits = len(set(recommended) & set(relevant))
    return hits / k


def recall_at_k(recommended, relevant, k=5):
    recommended = recommended[:k]
    hits = len(set(recommended) & set(relevant))
    return hits / len(relevant)


def ndcg_at_k(recommended, relevant, k=5):
    dcg = 0
    for i, item in enumerate(recommended[:k]):
        if item in relevant:
            dcg += 1 / math.log2(i + 2)

    ideal_dcg = sum(1 / math.log2(i + 2) for i in range(min(len(relevant), k)))
    return dcg / ideal_dcg if ideal_dcg > 0 else 0