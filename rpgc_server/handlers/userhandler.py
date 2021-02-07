from flask import Blueprint, request, jsonify
import logging
from marshmallow import ValidationError

from rpgc_server import db
from rpgc_server.resources.dbmodels import User
from rpgc_server.resources.user_forms import UserPostSchema

log = logging.getLogger('user_handler')
UserHandler = Blueprint('users', __name__)


@UserHandler.route('/', methods=["POST"])
def create_user():
    """creates new user, returns uuid, does not require auth"""

    schema = UserPostSchema()

    try:
        data = schema.load(request.args)
        # TODO check if user with given username/email/both exists already
        user = User(username=data['username'], email=data['email'], password=data['password'])

        db.session.add(user)
        db.session.commit()
    except ValidationError as err:
        print('zepsules', err.messages)
        print(err.valid_data)
        return err.messages, 400


@UserHandler.route('/<user_id>', methods=["GET"])
def get_user(user_id):
    """gets public profile of user with given uuid"""

    try:
        return jsonify(User.query.get(user_id))
    except Exception as e:  # TODO replace with proper exception handling (specific exception)
        log.warning(str(e))
        return 400


@UserHandler.route('/my', methods=["GET"])
def get_own_profile():
    """returns the profile of current user"""

    user_id = None  # auth.current_user()  # the auth should return uuid of currently authenticated user
    return jsonify(User.query.get(user_id))


@UserHandler.route('/<user_id>', methods=["PUT"])
def modify_user(user_id):
    """modifies the user with given id"""
    pass


@UserHandler.route('/', methods=["DELETE"])
def delete_user():
    """deletes user profile"""
    pass
