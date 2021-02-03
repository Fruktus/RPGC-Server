"""container for all data classes"""
import datetime
import uuid
from dataclasses import dataclass

from sqlalchemy.dialects.postgresql import UUID

from rpgc_server import db


@dataclass
class User(db.Model):
    __tablename__ = 'users'

    id: uuid.uuid4 = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    username: str = db.Column(db.String)
    password: str = db.Column(db.String)  # TODO maybe some way to enforce receiving password only in encrypted form?
    created_date: datetime = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    email: str = db.Column(db.String)
    rooms_owned: list = db.relationship('Room')

    # is_deleted = Column(Boolean)  # TODO decide whether to go this way (soft delete) or not

    def __repr__(self):
        return "<User(name='%s', pw='%s', email='%s')>" % (
            self.username, self.password, self.email)


@dataclass
class Room(db.Model):
    __tablename__ = 'rooms'

    id: uuid.uuid4 = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    owner_id: uuid.uuid4 = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'))
    owner = db.relationship('User', back_populates='rooms_owned')  # FIXME why are there two owner entries?
    name: str = db.Column(db.String)
    visible: bool = db.Column(db.Boolean, default=True)
    password: str = db.Column(db.String(30), nullable=True, default=None)  # if null then no password required

    users = db.relationship('User')  # TODO check if correct

    def __repr__(self):
        return "<Room(owner_id='%s', name='%s', visible='%s', password='%s')>" % (
            self.owner_id, self.name, self.visible, self.password)


@dataclass
class Message(db.Model):
    __tablename__ = 'messages'

    room_id: uuid.uuid4() = db.Column(UUID(as_uuid=True), db.ForeignKey('rooms.id'), primary_key=True,
                                      default=uuid.uuid4,
                                      unique=True, nullable=False)  # composite key from room uuid and serial
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True,
                        nullable=False)  # TODO: use serial/bigserial?
    author: uuid.uuid4() = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'))
    data: str = db.Column(db.String)  # for message body
    timestamp: datetime = db.Column(db.DateTime, default=datetime.datetime.utcnow)  # TODO check if type correct

    def __repr__(self):
        return "<Message(room_id='%s', id='%s', author='%s', data='%s', timestamp='%s')>" % (
            self.room_id, self.id, self.author, self.data, self.timestamp)


@dataclass
class Preset(db.Model):
    # info: this one is for users only, cannot be used directly in message as formatting, you need to use data
    # ie, treat this as macro, so that when user enters preset it should be converted in client to full format before
    # being sent to others
    __tablename__ = 'presets'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    user: uuid.uuid4() = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'))
    name: str = db.Column(db.String(64))
    # user = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    data: str = db.Column(db.String)

    def __repr__(self):
        return "<Preset(id='%s', user='%s', name='%s', data='%s')>" % (
            self.id, self.user, self.name, self.data)


@dataclass
class File(db.Model):
    __tablename__ = 'files'

    id: uuid.uuid4() = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    room_id: uuid.uuid4() = db.Column(UUID(as_uuid=True), db.ForeignKey('rooms.id'))
    owner: uuid.uuid4() = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'))
    name: str = db.Column(db.String)
    date_added: datetime = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<File(id='%s', room_id='%s', owner='%s', name='%s', date_added='%s')>" % (
            self.id, self.room_id, self.owner, self.name, self.date_added)


@dataclass
class Invitations(db.Model):
    __tablename__ = 'invitations'

    id: str = db.Column(db.String, primary_key=True, unique=True, nullable=False)  # mark as primary
    room_id: uuid.uuid4() = db.Column(UUID(as_uuid=True), db.ForeignKey('rooms.id'))
    expiration_date: datetime = db.Column(db.DateTime)
