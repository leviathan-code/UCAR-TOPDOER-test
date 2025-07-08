from sqlalchemy import (
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///./reviews.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
BaseSqlalchemyModel = declarative_base()


def get_session():
    with SessionLocal() as session:
        yield session
