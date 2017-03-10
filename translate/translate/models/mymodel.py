from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    TIMESTAMP,
    Boolean
)


from .meta import Base

import datetime


# class MyModel(Base):
#     __tablename__ = 'models'
#     id = Column(Integer, primary_key=True)
#     name = Column(Text)
#     value = Column(Integer)


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    password = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    admin = Column(Boolean, nullable=False)
    add_timestamp = Column(TIMESTAMP, nullable=False, default=datetime.datetime.now())
    update_timestamp = Column(TIMESTAMP, nullable=False, default=datetime.datetime.now())


class Language(Base):
    __tablename__= 'language'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    japanese = Column(Text, nullable=False)
    english = Column(Text, nullable=False)
    chinese = Column(Text, nullable=False)
    lock = Column(Boolean, nullable=False)
    add_timestamp = Column(TIMESTAMP, nullable=False, default=datetime.datetime.now())
    update_timestamp = Column(TIMESTAMP, nullable=False, default=datetime.datetime.now())

# Index('my_index', MyModel.name, unique=True, mysql_length=255)