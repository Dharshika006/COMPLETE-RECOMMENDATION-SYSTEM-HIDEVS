from data.models import User, Content, Interaction

class UserRepository:
    def __init__(self, db):
        self.db = db

    def get_user(self, user_id):
        return self.db.query(User).filter(User.id == user_id).first()


class ContentRepository:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        return self.db.query(Content).all()


class InteractionRepository:
    def __init__(self, db):
        self.db = db

    def get_user_history(self, user_id):
        return self.db.query(Interaction).filter(
            Interaction.user_id == user_id
        ).all()

    def record_feedback(self, user_id, content_id, rating):
        interaction = Interaction(
            user_id=user_id,
            content_id=content_id,
            type="feedback",
            rating=rating
        )
        self.db.add(interaction)
        self.db.commit()