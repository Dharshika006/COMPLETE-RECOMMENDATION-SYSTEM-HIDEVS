from data.database import SessionLocal
from data.models import User, Interaction


def test_seeded_user_exists():
    db = SessionLocal()
    user = db.query(User).filter(User.id == 1).first()
    assert user is not None


def test_seeded_interactions_exist():
    db = SessionLocal()
    interactions = db.query(Interaction).count()
    assert interactions > 0