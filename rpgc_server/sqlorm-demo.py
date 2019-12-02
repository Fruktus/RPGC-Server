import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from rpgc_server.resources.models import User, Base, Room

logging.basicConfig(level=logging.INFO)

engine = create_engine('sqlite:///:memory:', echo=False)  # does not use actual db, memory only
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)  # class template
session = Session()  # build class


ed_user = User(username='ed', password='pass', email='ed@uard.o')
print(ed_user)
import uuid
ed_user.id = uuid.uuid4()
print('ed uuid: ', ed_user.id)

session.add(ed_user)  # added to session, adding to database pending

our_user = session.query(User).filter_by(username='ed').first()  # retrieveing data, causes flushing pending operations
print(ed_user is our_user)  # true

session.add_all([  # multiple objects at once
        User(id=uuid.uuid4(), username='wendy', password='Wendy Williams', email='windy'),
        User(id=uuid.uuid4(), username='mary', password='Mary Contrary', email='mary'),
        User(id=uuid.uuid4(), username='fred', password='Fred Flintstone', email='freddy')])


print(session.dirty)  # shows modified data
print(session.new)  # shows added data

ed_user.rooms_owned = [
    Room(id=uuid.uuid4(), name='DnD', visible=True),
    Room(id=uuid.uuid4(), name='AT', visible=False, password='ark')
]

session.commit()  # flushes data
