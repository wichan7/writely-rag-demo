from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('postgresql://postgres:990909@localhost:5432/mydb')

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

Base = declarative_base()