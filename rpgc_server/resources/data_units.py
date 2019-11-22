"""container for all data classes"""
from sqlalchemy import Column, Integer, String

# FIXME do note that everything here at the moment is just a draft
# SELF: look here: https://docs.sqlalchemy.org/en/13/orm/tutorial.html


class User:
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    nickname = Column(String)
    fullname = Column(String)  # demo only


class Room:
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True)
    owner = Column(String)
    # users = array?


class Message:
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    # possibly room id as foreign key


class Preset:
    # info: this one is for users only, cannot be used directly in message as formatting, you need to use data
    __tablename__ = 'presets'

    id = Column(Integer, primary_key=True)
    # user id as foreign key
    # data - how preset looks like
