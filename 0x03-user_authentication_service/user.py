#!/usr/bin/env python3
"""A module that defines a User model in SQLAlchemy."""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class User(Base):
    """A class that represents the user in the users table.
    """
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True, nullable=False)
    email: str = Column(String(250), nullable=False)
    hashed_password: str = Column(String(250), nullable=False)
    session_id: str = Column(String(250), nullable=True)
    reset_token: str = Column(String(250), nullable=True)
