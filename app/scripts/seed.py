from app.infrastructure.db.session import SessionLocal, engine
from app.infrastructure.db.base import Base
from app.infrastructure.db.models import User, Task

def run():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    alice = User(email="alice@example.com", name="Alice", password="alice123")
    bob = User(email="bob@example.com", name="Bob", password="bob123")
    db.add_all([alice, bob])
    db.flush()
    t1 = Task(title="Onboard", description="Read docs", owner_id=alice.id)
    t2 = Task(title="Setup PC", description="Install tools", owner_id=bob.id)
    db.add_all([t1, t2])
    db.commit()

if __name__ == "__main__":
    run()
