from data.database import SessionLocal
from data.models import User

def test_user_insert():
    db = SessionLocal()
    user = db.query(User).filter(User.id == 1).first()
    assert user is not None