from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from rpgc_server import db
from rpgc_server.resources.dbmodels import Room
from rpgc_server.resources.user_forms import RoomPostSchema

RoomHandler = Blueprint('rooms', __name__)


@RoomHandler.route('/<room_id>', methods=["GET"])
def get_room(room_id: str):
    """retrieves room by uuid if user has permissions to view it"""
    try:
        return jsonify(Room.query.get(room_id))
    except Exception as e:  # TODO replace with proper exception handling (specific exception)
        return 400


@RoomHandler.route('/visible', methods=["GET"])
def get_visible_rooms(room_id: str):
    """retrieves room by uuid if user has permissions to view it"""
    try:

        return jsonify(Room.query.filter(Room.visible))
    except Exception as e:  # TODO replace with proper exception handling (specific exception)
        return 400


@RoomHandler.route('/my', methods=["GET"])
def get_my_rooms():
    """retrieves all rooms owned by user (user id obtained from auth)"""

    user_id = None  # auth.current_user()  # FIXME check, implement

    try:
        return jsonify(Room.query.filter(Room.owner_id == user_id))  # check whether "in" works
    except Exception as e:  # TODO replace with proper exception handling (specific exception)
        return 400


@RoomHandler.route('/joined', methods=["GET"])
def get_joined_rooms():
    """retrieves all rooms that user is part of (user id obtained from auth)"""

    user_id = None  # auth.current_user()  # FIXME check, implement

    try:
        return jsonify(Room.query.filter(Room.owner_id == user_id or user_id in Room.users))  # TODO
        # replace with proper fetching (currently code is a placeholder)
    except Exception as e:  # TODO replace with proper exception handling (specific exception)
        return 400


@RoomHandler.route('/', methods=["POST"])
def create_room():
    """creates new room on server based on parameters, returns uuid of the room"""

    schema = RoomPostSchema()
    # TODO grab owner from auth, by default creator is always owner
    # it will be possible to give room to someone else later

    try:
        data = schema.load(request.args)
        # TODO check if room with given name (?) exists
        room = Room(owner_id=data['owner_id'], name=data['name'], password=data['password'], visible=data['visible'])

        db.session.add(room)
        db.session.commit()
        return jsonify(room), 201
    except ValidationError as err:
        print('zepsules', err.messages)
        print(err.valid_data)


@RoomHandler.route('/<room_id>', methods=["PUT"])
def modify_room(room_id):
    """changes settings of room given by room_id if user is the owner"""
    pass


@RoomHandler.route('/<room_id>', methods=["DELETE"])
def delete_room(room_id):
    """marks the room as deleted"""
    # TODO maybe only if no people inside
    pass


@RoomHandler.route('/<room_id>', methods=["PUT"])
def leave_room(room_id):
    """removes current player (obtained from auth) from given room"""
    user_id = None  # get from auth  TODO
    room = Room.query.get(room_id)
    room.users.remove(user_id)


# @RoomHandler.route('/<room_id>/messages/', methods=["GET"])
# def get_message():
#     pass

# TODO decide how to access messages, think whether provide endpoint for bulk request for many messages
# TODO (better performance?) and whether it should be in this file or different one
