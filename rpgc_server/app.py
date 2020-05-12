from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy  # possibly may not be needed


auth = HTTPBasicAuth()
app = Flask(__name__)
# FIXME: add proper secret key
app.config.from_pyfile('config_test.cfg')

db = SQLAlchemy(app)  # https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
socketio = SocketIO(app)

# HOWTO: socketio without decorator: socketio.on_event('my event', my_function_handler, namespace='/test')
# HOWTO: split into rooms: Do an authenticated connection to /channel/{roomId}
# HOWTO: nvm the above, there is example in docs: https://flask-socketio.readthedocs.io/en/latest/
# HOWTO: most likely I'll expose single endpoint, /channel, to which clients will connect passing room as parameter
# (possibly in every message)

# socket test: https://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent
# input validation: https://flask-marshmallow.readthedocs.io/en/latest/

users = {  # DBG testing only, for removal
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


@auth.login_required
@app.route('/api/v1.0/users/<int:user_id>', methods=['GET'])
def user_get(user_id):
    return str(request.data) + ' ' + str(user_id)
    # try:
    #     # get user data by uuid
    #     # TODO idk how to retrieve data from db at the moment, replace the dict with call to db
    #     return UserGetSchema().load({"name": "Ronnie", "email": "invalid"})
    # except ValidationError as err:
    #     # TODO return some html like missing param or smth
    #     print(err.messages)
    #     print(err.valid_data)
    #     return 422  # unprocessable entity - server understood the request but cannot process it
    # ^ unnecessary, the users will be exposed as endpoint, so no need to authenticate additionaly


@auth.login_required
@app.route('/api/v1.0/users/<int:user_id>', methods=['PUT'])
def user_put(user_id):
    # user_schema = UserSchema()
    # try:
    #     user = UserSchema().load({"name": "Ronnie", "email": "invalid"})
    # except ValidationError as err:
    #     print(err.messages)
    #     print(err.valid_data)
    pass


@app.route('/api/v1.0/users', methods=['POST'])
def user_post():
    pass


@auth.login_required
@app.route('/api/v1.0/users/<int:user_id>', methods=['DELETE'])
def user_delete(user_id):
    pass


@auth.login_required
@app.route('/api/v1.0/rooms/<int:room_id>', methods=['GET'])
def room_get(room_id):
    # get room data by uuid
    # different action when called without parameter (get all)
    return "it works! RoomHandler"


@auth.login_required
@app.route('/api/v1.0/rooms/my/<int:user_id>', methods=['GET'])
def room_get_my(self):
    # just a test for binding to specific sub-url
    return "it works! custom endpoint RoomHandler"


@auth.login_required
@app.route('/api/v1.0/rooms/<int:room_id>', methods=['PUT'])
def room_put(room_id):
    # create
    pass


@auth.login_required
@app.route('/api/v1.0/rooms', methods=['POST'])
def room_post():
    # update
    pass


@auth.login_required
@app.route('/api/v1.0/rooms/<int:room_id>', methods=['DELETE'])
def room_delete(self):
    pass


@auth.login_required
@app.route('/api/v1.0/messages/<int:room_id>/<int:message_id>', methods=['GET'])
def message_get(room_id, message_id):
    pass


@auth.login_required
@app.route('/api/v1.0/messages/<int:room_id>>', methods=['POST'])
def message_post(room_id):
    pass


@auth.login_required
@app.route('/api/v1.0/messages/<int:room_id>/<int:message_id>', methods=['PUT'])
def message_put(room_id, message_id):
    pass


@auth.login_required
@app.route('/api/v1.0/messages/<int:room_id>/<int:message_id>', methods=['DELETE'])
def message_delete(room_id, message_id):
    pass


@auth.login_required
@app.route('/api/v1.0/presets/<int:preset_id>', methods=['GET'])
def preset_get(preset_id):
    pass


@auth.login_required
@app.route('/api/v1.0/presets/my/<int:user_id>', methods=['GET'])
def preset_my(user_id):
    pass


@auth.login_required
@app.route('/api/v1.0/presets/<int:user_id>', methods=['POST'])
def preset_post(user_id):
    pass


@auth.login_required
@app.route('/api/v1.0/presets/<int:preset_id>', methods=['PUT'])
def preset_put(preset_id):
    pass


@auth.login_required
@app.route('/api/v1.0/presets/<int:preset_id>', methods=['DELETE'])
def preset_delete(preset_id):
    pass


@auth.login_required
@app.route('/api/v1.0/media/<int:room_id>/<int:user_id>/<str:filename>', methods=['GET'])
def media_get(room_id, user_id, filename):
    pass


@auth.login_required
@app.route('/api/v1.0/media/<int:room_id>/<int:user_id>/<str:filename>', methods=['POST'])
def media_post(room_id, user_id, filename):
    pass


@auth.login_required
@app.route('/api/v1.0/media/<int:room_id>/<int:user_id>/<str:filename>', methods=['PUT'])
def media_put(room_id, user_id, filename):
    pass


@auth.login_required
@app.route('/api/v1.0/media/<int:room_id>/<int:user_id>/<str:filename>', methods=['DELETE'])
def media_delete(room_id, user_id, filename):
    # TODO possibly will not be available
    pass

# class AuthDemo(Resource):
#     # method_decorators = {'get': [auth.login_required]}  # will apply auth to get
#
#     def get(self):
#         return {'auth': 'ok'}


# dynamically modify base class to include the auth method
# TODO will most likely be required for every class since the auth is dynamically created
# AuthDemo.method_decorators = {'get': [auth.login_required]}  # possibly i should save the result or smth


if __name__ == '__main__':
    # app.run()  # DBG most likely not needed, since socketio does that already
    socketio.run(app)
    # socketio.run(app, host='0.0.0.0', debug=True, keyfile='key.pem', certfile='cert.pem')  # how to ssl
