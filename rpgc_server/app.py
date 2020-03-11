from flask import Flask, request
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy  # possibly may not be needed

from rpgc_server.resources.routes import UserHandler, RoomHandler

auth = HTTPBasicAuth()
app = Flask(__name__)
# FIXME: add proper secret key
app.config.from_pyfile('config_test.cfg')

api = Api(app)
db = SQLAlchemy(app)  # https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
socketio = SocketIO(app)

# HOWTO: socketio without decorator: socketio.on_event('my event', my_function_handler, namespace='/test')
# HOWTO: split into rooms: Do an authenticated connection to /channel/{roomId}
# HOWTO: nvm the above, there is example in docs: https://flask-socketio.readthedocs.io/en/latest/
# HOWTO: most likely I'll expose single endpoint, /channel, to which clients will connect passing room as parameter
# (possibly in every message)

# socket test: https://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent
# input validation: https://flask-marshmallow.readthedocs.io/en/latest/

users = {
    # "john": generate_password_hash("hello"), # TODO: hash password! db can handle encryption etc, check that
    "john": "hello",
    "susan": "bye"
}


@auth.verify_password
def verify_password(username, password):
    if username in users:
        # TODO: hash password!
        # return check_password_hash(users.get(username), password)
        return users.get(username) == password
    return False


class HelloWorld(Resource):
    # DBG test only, to check whether the object state is kept (it is)
    counter = 0

    def get(self):
        HelloWorld.counter += 1
        return {'hello': str(HelloWorld.counter)}


class AuthDemo(Resource):
    # method_decorators = {'get': [auth.login_required]}  # will apply auth to get

    def get(self):
        return {'auth': 'ok'}


# dynamically modify base class to include the auth method
# TODO will most likely be required for every class since the auth is dynamically created
AuthDemo.method_decorators = {'get': [auth.login_required]}  # possibly i should save the result or smth

# setup the resources
api.add_resource(HelloWorld, '/', '/hello')  # DBG demo only
api.add_resource(AuthDemo, '/auth')

api.add_resource(UserHandler, '/users')  # possibly add specific urls to those
# api.add_resource(RoomHandler.get_my, '/rooms/my')  # attempt to expose specific methods with one class
api.add_resource(RoomHandler, '/rooms')


if __name__ == '__main__':
    # app.run()  # DBG most likely not needed, since socketio does that already
    socketio.run(app)
    # socketio.run(app, host='0.0.0.0', debug=True, keyfile='key.pem', certfile='cert.pem')  # how to ssl
