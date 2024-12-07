from sqlalchemy import Column, String, Integer
from src.core.db import Base

class Document(Base):
    __tablename__ = 'document'

    id = Column(Integer, primary_key=True)
    content = Column(String)

    def __init__(self, id, content):
        self.id = id
        self.content = content