from flask import Flask, request
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

users = {
    # "john": generate_password_hash("hello"),
    "john": "hello",
    "susan": "bye"
}


@auth.verify_password
def verify_password(username, password):
    if username in users:
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
    app.run()
