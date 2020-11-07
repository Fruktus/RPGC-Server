from flask import Blueprint

RoomHandler = Blueprint('rooms', __name__)


# @RoomHandler.route('/', methods=["GET"], defaults={'page': 'index'})
# @RoomHandler.route('/<page>', methods=["GET"])
# @auth.login_required
# def index(page):
#     try:
#         if page == 'E1M1.mp3':
#             # return send_from_directory('templates/funstuff/', 'E1M1.mp3')
#         return render_template('funstuff/%s.html' % page.replace('.html', ''))
#     except TemplateNotFound:
#         abort(404)

@RoomHandler.route('/<room_id>', methods=["GET"])
def get_room(room_id: str):
    """retrieves room by uuid if user has permissions to view it"""
    # retrieve, return
    pass


@RoomHandler.route('/my', methods=["GET"])
def get_my_rooms():
    """retrieves all rooms owned by user (user id obtained from auth)"""
    pass


@RoomHandler.route('/', methods=["POST"])
def create_room():
    """creates new room on server based on parameters, returns uuid of the room"""


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
    pass
