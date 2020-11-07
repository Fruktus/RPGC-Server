"""container for all data classes"""
import datetime
# from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
# from sqlalchemy.orm import relationship
import uuid

from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy_utils import UUIDType


from rpgc_server import db

# https://docs.sqlalchemy.org/en/13/orm/tutorial.html
# https://websauna.org/docs/narrative/modelling/models.html#primary-keys-uuid-running-counter-or-both
# ^ how to enable uuids in postgresql
# https://docs.sqlalchemy.org/en/13/core/custom_types.html#backend-agnostic-guid-type


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    username = db.Column(db.String)
    password = db.Column(db.String)
    # TODO: password should be hash (will be hashed when creating user)
    # check here: https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html#module-sqlalchemy_utils.types.encrypted.encrypted_type
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    email = db.Column(db.String)
    rooms_owned = db.relationship('Room')
    # is_deleted = Column(Boolean)

    def __repr__(self):
        return "<User(name='%s', pw='%s', email='%s')>" % (
            self.username, self.password, self.email)


class Room(db.Model):
    __tablename__ = 'rooms'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    owner_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'))  # FIXME why are there two of these?
    owner = db.relationship('User', back_populates='rooms_owned')
    name = db.Column(db.String)
    visible = db.Column(db.Boolean)
    password = db.Column(db.String(30), nullable=True)  # if null then no password required
    # users = array? -> requires additional table connecting rooms and users # TODO implement that


class Message(db.Model):
    __tablename__ = 'messages'

    room_id = db.Column(UUID(as_uuid=True), db.ForeignKey('rooms.id'), primary_key=True, default=uuid.uuid4,
                        unique=True, nullable=False)  # composite key from room uuid and serial
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)  # TODO: use serial/bigserial? also: rename field
    author = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'))
    data = db.Column(db.String)  # for message body
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)  # TODO check if type correct


class Preset(db.Model):
    # info: this one is for users only, cannot be used directly in message as formatting, you need to use data
    __tablename__ = 'presets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    user = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'))
    name = db.Column(db.String(64))
    # user = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    data = db.Column(db.String)


# TODO separate model for files? models for websockets

class File(db.Model):
    __tablename__ = 'files'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)  # FIXME check
    room_id = db.Column(UUID(as_uuid=True), db.ForeignKey('rooms.id'))
    owner = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'))
    name = db.Column(db.String)
    date_added = db.Column(db.DateTime, default=datetime.datetime.utcnow)


class Invitations(db.Model):
    __tablename__ = 'invitations'

    id = db.Column(db.String, primary_key=True, unique=True, nullable=False)  # mark as primary
    room_id = db.Column(UUID(as_uuid=True), db.ForeignKey('rooms.id'))
    expiration_date = db.Column(db.DateTime)
