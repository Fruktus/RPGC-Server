"""contains classes for websocket rooms"""
from flask_socketio import join_room, leave_room, send


# SAMPLES:
# @socketio.on('join')  # will be added in main file
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(username + ' has entered the room.', room=room)


# @socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', room=room)


# @socketio.on('message')
def handle_message(message):
    print('received message: ' + message)


# @socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))
    send(json, json=True, namespace='/chat')  # bounces back json


# @socketio.on('my event')
def handle_my_custom_event(arg1, arg2, arg3):
    print('received args: ' + arg1 + arg2 + arg3)
    return 'one', 2  # will be sent back through callback as parameters


# @socketio.on('my event', namespace='/test')
def handle_my_custom_namespace_event(json):
    print('received json: ' + str(json))

