"""container for all data classes"""
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.dialects.postgresql import UUID

# FIXME do note that everything here at the moment is just a draft
# SELF: look here: https://docs.sqlalchemy.org/en/13/orm/tutorial.html
# SELF: https://websauna.org/docs/narrative/modelling/models.html#primary-keys-uuid-running-counter-or-both
# ^ how to enable uuids in postgresql


class User:
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True)
    username = Column(String)
    password = Column(String)  # TODO: should be hashed
    email = Column(String)


class Room:
    __tablename__ = 'rooms'

    id = Column(UUID(as_uuid=True), primary_key=True)
    owner = Column(String(64),  # FIXME, will not be a string, figure out how to use foriegnkey
                   index=False,
                   # ForeignKey("user.user_id")  # is most commonly a string of the form <tablename>.<columnname>
                   unique=False,
                   nullable=False)
    visible = Column(Boolean)
    password = Column(String(30),
                      nullable=True)  # if null then no password required
    # users = array? -> requires additional table connecting rooms and users

# how-to association table:
# class Actor(Base):
#     __tablename__ = 'actors'
#
#     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     name = Column(String)
#     nickname = Column(String)
#     academy_awards = Column(Integer)
#
# class Movie(Base):
#     __tablename__ = 'movies'
#
#     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     title = Column(String)
#
#     actors = relationship('ActorMovie', uselist=True, backref='movies')
#
# class ActorMovie(Base):
#     __tablename__ = 'actor_movies'
#
#     actor_id = Column(UUID(as_uuid=True), ForeignKey('actors.id'))
#     movie_id = Column(UUID(as_uuid=True), ForeignKey('movies.id'))


class Message:
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    # TODO: possibly use uuid or create additional counter field for batch retrieval
    data = Column(String(100))  # for text 
    # possibly room id as foreign key


class Preset:
    # info: this one is for users only, cannot be used directly in message as formatting, you need to use data
    __tablename__ = 'presets'

    id = Column(Integer, primary_key=True)
    # user id as foreign key
    # data - how preset looks like


# TODO separate model for files? models for websockets
