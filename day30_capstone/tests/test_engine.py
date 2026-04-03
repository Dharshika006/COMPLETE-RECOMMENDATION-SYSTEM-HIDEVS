from engine.evaluator import precision_at_k

def test_precision():
    rec = [1, 2, 3, 4, 5]
    rel = [1, 2, 7]
    assert precision_at_k(rec, rel) == 0.4