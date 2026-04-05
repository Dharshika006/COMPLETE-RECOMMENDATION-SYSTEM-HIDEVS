from data.database import SessionLocal
from data.models import User, Content, Interaction


def test_seeded_user_exists():
    db = SessionLocal()
    user = db.query(User).filter(User.id == 1).first()
    assert user is not None


def test_seeded_content_exists():
    db = SessionLocal()
    content_count = db.query(Content).count()
    assert content_count >= 20


def test_seeded_interactions_exist():
    db = SessionLocal()
    interaction_count = db.query(Interaction).count()
    assert interaction_count > 0