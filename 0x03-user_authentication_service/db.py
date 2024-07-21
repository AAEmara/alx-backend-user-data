#!/usr/bin/env python3
"""DB module."""

from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Adds a new user to the database.
        Args:
            email: The user's email.
            hashed_password: the user's hashed password.
        Returns:
            A newly created User Class instance.
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return (new_user)

    def find_user_by(self, **kwargs):
        """Retrieves a User instance through using the given arbitrary keyword.
        Args:
            kwargs (any): An arbitrary keyword argument to search for.
        Returns:
            The User instance found.
        """
        for key, val in kwargs.items():
            if not hasattr(User, key):
                raise(InvalidRequestError)
            column = key
            value = val
        filter_stmt = f"{column}=:filter_value"
        try:
            user = self.__session.query(User).\
                filter(text(filter_stmt)).\
                params(filter_value=value).\
                one()
        except NoResultFound:
            raise(NoResultFound)
        return (user)
