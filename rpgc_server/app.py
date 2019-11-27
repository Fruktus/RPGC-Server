from flask import Flask, request
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from flask_socketio import SocketIO

auth = HTTPBasicAuth()
app = Flask(__name__)
# FIXME: add proper secret key
app.config['SECRET_KEY'] = 'secret!'
api = Api(app)
socketio = SocketIO(app)

# HOWTO: socketio without decorator: socketio.on_event('my event', my_function_handler, namespace='/test')
# HOWTO: split into rooms: Do and authenticated connection to /channel/{roomId}
# HOWTO: nvm the above, there is example in docs: https://flask-socketio.readthedocs.io/en/latest/

users = {
    # "john": generate_password_hash("hello"), # TODO: hash password!
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
