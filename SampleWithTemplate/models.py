#!/usr/bin/env python
from sqlalchemy import Column, Integer, String
from database import Base


class ActiveData(Base):
    __tablename__ = 'active_data'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    sentiment = Column(String(120), unique=True)

    def __init__(self, username=None, sentiment=None):
        self.username = username
        self.sentiment = sentiment

    def __repr__(self):
        return '<User %r>' % (self.username)
