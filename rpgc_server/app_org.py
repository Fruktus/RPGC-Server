from flask import Flask
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy  # possibly may not be needed

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
# input validation opt1: https://chrisalbon.com/python/basics/compare_two_dictionaries/
# opt2: https://flask-marshmallow.readthedocs.io/en/latest/

users = {
    # "john": generate_password_hash("hello"), # TODO: hash password! FOLLOWUP: db can handle encryption etc, check that
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
    counter = 0

    def get(self):
        HelloWorld.counter += 1
        return {'hello': str(HelloWorld.counter)}


# todos = {}
# class TodoSimple(Resource):
#     def get(self, todo_id):
#         return {todo_id: todos[todo_id]}
#
#     def put(self, todo_id):
#         todos[todo_id] = request.form['data']
#         return {todo_id: todos[todo_id]}

class AuthDemo(Resource):
    # method_decorators = {'get': [auth.login_required]}  # will apply auth to get

    def get(self):
        return {'auth': 'ok'}


# dynamically modify base class to include the auth method,
AuthDemo.method_decorators = {'get': [auth.login_required]}
# c = AuthDemo
# c.method_decorators = {'get': [auth.login_required]}
# api.add_resource(TodoSimple, '/<string:todo_id>')
api.add_resource(HelloWorld, '/', '/hello')
api.add_resource(AuthDemo, '/auth')


if __name__ == '__main__':
    # app.run()
    socketio.run(app)
    # socketio.run(app, host='0.0.0.0', debug=True, keyfile='key.pem', certfile='cert.pem')  # how to ssl
