from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:990909@localhost:5432/mydb')
# use session_factory() to get a new Session
_SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()

def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()