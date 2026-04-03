from data.database import Base, engine, SessionLocal
from data.models import User, Content

Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Add 10 users
for i in range(1, 11):
    db.add(User(
        id=i,
        name=f"User{i}",
        interests="AI,ML"
    ))

# Add 20 content items
categories = ["AI", "ML", "Data", "Python"]

for i in range(1, 21):
    db.add(Content(
        id=i,
        title=f"Course {i}",
        category=categories[i % 4],
        difficulty="medium",
        popularity=20 - i
    ))

db.commit()
print("Sample data inserted successfully.")