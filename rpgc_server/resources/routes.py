"""contains classes with REST handlers for data units"""
from flask_restful import Resource
from rpgc_server.resources.models import User, Room, Message, Preset


# sample handler
class UserHandler(Resource):
    def get(self):
        # get user data by uuid
        pass

    def put(self):
        pass

    def post(self):  # one of those unnecessary i think
        pass

    def delete(self):
        pass


class RoomHandler(Resource):
    def get(self):
        # get room data by uuid
        # different action when called without parameter (get all)
        pass

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
