"""container for all data classes"""
import datetime
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
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
    username = Column(String)  # non changeable
    password = Column(String)
    display_name = Column(String)
    # TODO: password should be hash (will be hashed when creating user)
    # check here: https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html#module-sqlalchemy_utils.types.encrypted.encrypted_type
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    email = Column(String)
    rooms_owned = relationship('Room')

    def __repr__(self):
        return "<User(name='%s', pw='%s', email='%s')>" % (
            self.username, self.password, self.email)


class Room(Base):
    __tablename__ = 'rooms'

    id = Column(UUIDType(), primary_key=True)
    owner_id = Column(UUIDType(), ForeignKey('users.id'))  # FIXME why are there two of these ids?
    owner = relationship('User', back_populates='rooms_owned')  # FIXME probably only this one should be left
    name = Column(String)
    visible = Column(Boolean)
    password = Column(String(30), nullable=True)  # if null then no password required
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
    user = Column(Integer, ForeignKey('users.id'))
    name = Column(String(64))  # unique in user scope
    # user = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    data = Column(String)


# TODO separate model for files? models for websockets
# Followup: files will be managed manually

class Media(Base):
    # just a draft
    # the users will upload any number of files for a room
    # the files will have a name known to user and only that user can reference that file
    # (or should i allow public files?)
    # anyway the primary key should be combo of roomid, userid and the filename
    # the filenames have to be unique for any given room and user
    __tablename__ = 'media'

    room_id = Column(UUIDType(), ForeignKey('rooms.id'), primary_key=True)  # composite key from room uuid and serial
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    filename = Column(Integer, primary_key=True)
    data_path = Column(String)  # data will be path to file
    # when uploading file, it will be saved in system in corresponding folder with new name
    # there wont be an option to modify or remove once uploaded file (well, maybe if it wasnt referenced yet)
    # except for deletion of whole room, which would remove its data folder
