from engine.evaluator import precision_at_k, recall_at_k, ndcg_at_k

def test_precision():
    assert precision_at_k([1,2,3,4,5], [1,3,5], 5) > 0

def test_recall():
    assert recall_at_k([1,2,3,4,5], [1,3,5], 5) == 1.0

def test_ndcg():
    assert ndcg_at_k([1,2,3,4,5], [1,3,5], 5) > 0