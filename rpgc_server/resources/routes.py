"""contains classes with REST handlers for data units"""
from flask_restful import Resource
from marshmallow import ValidationError

from rpgc_server.resources.models import User, Room, Message, Preset

from rpgc_server.resources.user_forms import UserGetSchema


# sample handler


class UserHandler(Resource):
    def get(self):
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
        pass

    def put(self):
        # user_schema = UserSchema()
        # try:
        #     user = UserSchema().load({"name": "Ronnie", "email": "invalid"})
        # except ValidationError as err:
        #     print(err.messages)
        #     print(err.valid_data)
        pass

    def post(self):  # one of those unnecessary i think
        pass

    def delete(self):
        pass


class RoomHandler(Resource):
    def get(self):
        # get room data by uuid
        # different action when called without parameter (get all)
        return "it works! RoomHandler"

    def get_my(self):
        # just a test for binding to specific sub-url
        return "it works! custom endpoint RoomHandler"

    def put(self):
        # create
        pass

    def post(self):
        # update
        pass

    def delete(self):
        pass

# @app.route('/', methods=['GET'])
# def create_user():
#     """Create a user."""
#     username = request.args.get('user')
#     email = request.args.get('email')
#     if username and email:
#         existing_user = User.query.filter(User.username == username or User.email == email).first()
#         if existing:
#             return make_response(f'{username} ({email}) already created!')
#         new_user = User(username=username,
#                         email=email,
#                         created=dt.now(),
#                         bio="In West Philadelphia born anised, on the playground is where I spent most of my days",
#                         admin=False)  # Create an instance of the User class
#         db.session.add(new_user)  # Adds new User record to database
#         db.session.commit()  # Commits all changes
#     return make_response(f"{new_user} successfully created!")
