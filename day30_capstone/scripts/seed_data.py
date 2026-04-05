from data.database import Base, engine, SessionLocal
from data.models import User, Content, Interaction


def seed():
    # create tables
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    # clear old data for reproducibility
    db.query(Interaction).delete()
    db.query(Content).delete()
    db.query(User).delete()
    db.commit()

    # -----------------------------
    # seed users
    # -----------------------------
    users = [
        User(id=1, name="Alice", interests="AI,Python"),
        User(id=2, name="Bob", interests="ML,Data"),
        User(id=3, name="Charlie", interests="Python,Web"),
        User(id=4, name="David", interests="AI,ML"),
        User(id=5, name="Eva", interests="Data,SQL"),
        User(id=6, name="Frank", interests="Python,ML"),
        User(id=7, name="Grace", interests="AI,Data"),
        User(id=8, name="Helen", interests="Web,Python"),
        User(id=9, name="Ian", interests="ML,AI"),
        User(id=10, name="Julia", interests="Data,Python"),
    ]
    db.add_all(users)

    # -----------------------------
    # seed content
    # -----------------------------
    categories = ["AI", "ML", "Data", "Python"]

    content_items = []
    for i in range(1, 21):
        category = categories[(i - 1) % len(categories)]
        content_items.append(
            Content(
                id=i,
                title=f"Course {i}",
                category=category,
                difficulty="Intermediate",
                popularity=100 - i,
            )
        )

    db.add_all(content_items)

    # -----------------------------
    # seed realistic interactions
    # -----------------------------
    interactions = [
        # user 1 strongly likes AI/Python
        Interaction(user_id=1, content_id=1, type="view", rating=5),
        Interaction(user_id=1, content_id=4, type="view", rating=5),
        Interaction(user_id=1, content_id=5, type="view", rating=4),

        # user 2 likes ML/Data
        Interaction(user_id=2, content_id=2, type="view", rating=5),
        Interaction(user_id=2, content_id=3, type="view", rating=4),

        # user 3 likes Python/Web style content
        Interaction(user_id=3, content_id=4, type="view", rating=5),
        Interaction(user_id=3, content_id=8, type="view", rating=4),

        # user 4 AI + ML
        Interaction(user_id=4, content_id=1, type="view", rating=5),
        Interaction(user_id=4, content_id=2, type="view", rating=5),

        # user 5 data-focused
        Interaction(user_id=5, content_id=3, type="view", rating=5),
        Interaction(user_id=5, content_id=7, type="view", rating=4),

        # extra mixed behavior
        Interaction(user_id=6, content_id=6, type="view", rating=4),
        Interaction(user_id=7, content_id=9, type="view", rating=5),
        Interaction(user_id=8, content_id=12, type="view", rating=3),
        Interaction(user_id=9, content_id=15, type="view", rating=4),
        Interaction(user_id=10, content_id=18, type="view", rating=5),
    ]

    db.add_all(interactions)
    db.commit()
    db.close()

    print("✅ Database seeded successfully with users, content, and interactions.")


if __name__ == "__main__":
    seed()