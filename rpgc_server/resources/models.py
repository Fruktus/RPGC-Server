"""container for all data classes"""
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_utils import UUIDType
from sqlalchemy.ext.declarative import declarative_base

# FIXME do note that everything here at the moment is just a draft
# SELF: look here: https://docs.sqlalchemy.org/en/13/orm/tutorial.html
# SELF: https://websauna.org/docs/narrative/modelling/models.html#primary-keys-uuid-running-counter-or-both
# ^ how to enable uuids in postgresql
# https://docs.sqlalchemy.org/en/13/core/custom_types.html#backend-agnostic-guid-type

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(UUIDType(), primary_key=True)
    username = Column(String)
    password = Column(String)  # TODO: should be hash (will be hashed when creating user)
    email = Column(String)
    rooms_owned = relationship('Room')

    def __repr__(self):
        return "<User(name='%s', pw='%s', email='%s')>" % (
            self.username, self.password, self.email)


class Room(Base):
    __tablename__ = 'rooms'

    id = Column(UUIDType(), primary_key=True)
    owner_id = Column(UUIDType(), ForeignKey('users.id'))
    owner = relationship('User', back_populates='rooms_owned')
    name = Column(String)
    visible = Column(Boolean)
    password = Column(String(30),
                      nullable=True)  # if null then no password required
    # users = array? -> requires additional table connecting rooms and users


class Message(Base):
    __tablename__ = 'messages'

    room_id = Column(UUIDType(), ForeignKey('rooms.id'), primary_key=True)  # composite key from room uuid and serial
    id = Column(Integer, primary_key=True)  # TODO: use serial/bigserial? also: rename field
    author = Column(UUIDType(), ForeignKey('users.id'))
    data = Column(String)  # for text


class Preset(Base):
    # info: this one is for users only, cannot be used directly in message as formatting, you need to use data
    __tablename__ = 'presets'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    # user = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    user = Column(Integer, ForeignKey('users.id'))
    data = Column(String)


# TODO separate model for files? models for websockets
