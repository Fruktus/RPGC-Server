from flask import Blueprint

UserHandler = Blueprint('users', __name__)


@UserHandler.route('/', methods=["POST"])
def create_user():
    """creates new user, returns uuid, does not require auth"""
    pass


@UserHandler.route('/<user_id>', methods=["GET"])
def get_user(user_id):
    """gets public profile of user with given uuid"""
    pass


@UserHandler.route('/my', methods=["GET"])
def get_own_profile():
    """returns the profile of current user"""
    pass


@UserHandler.route('/<user_id>', methods=["PUT"])
def modify_user(user_id):
    """modifies the user with given id"""
    pass


@UserHandler.route('/', methods=["DELETE"])
def delete_user():
    """deletes user profile"""
    pass
