# coding=utf-8

from sqlalchemy import Column, String, Sequence
from src.core.db import Base


class Document(Base):
    __tablename__ = 'document'

    id = Column(Sequence, primary_key=True)
    content = Column(String)

    def __init__(self, content):
        self.content = content