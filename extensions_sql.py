from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker

db = SQLAlchemy()


def get_session(bind_key=None):
    """Return a new session using the specified bind key."""
    if bind_key:
        engine = db.engines[bind_key]
    else:
        engine = db.engine
    session = sessionmaker(bind=engine)
    return session()
