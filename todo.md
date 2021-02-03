/players -> uuid
	create -> uuid
	get_self -> info o profilu
	get -> uuid
	delete
	update -> null


/rooms
	create
	get
	get_my
	get_joined

	<roomid>/messages/<messageid>


/messages

/files/<uuid>

baza:
	uuid: owner, room, name, path

check whether possible to upload file with changed name

## setting up postgres:
create database rpgc_test;
create user test with encrypted password 'test';
grant all privileges on database rpgc_test to test;

## basic test:
from rpgc_server import db
from rpgc_server.resources.dbmodels import User

db.create_all()
u = User(username='alfred', password='asd', email='asd')
db.session.add(u)
db.session.commit()