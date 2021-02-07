from rpgc_server import app, log, auth, chats
from rpgc_server.handlers.messagehandler import MessageHandler
from rpgc_server.handlers.presethandler import PresetHandler
from rpgc_server.handlers.roomhandler import RoomHandler
from rpgc_server.handlers.userhandler import UserHandler

# adding bp
app.register_blueprint(RoomHandler, url_prefix='/rooms')
app.register_blueprint(MessageHandler, url_prefix='/messages')
app.register_blueprint(UserHandler, url_prefix='/users')
app.register_blueprint(PresetHandler, url_prefix='/presets')


@auth.verify_password
def verify_password(username, password):
    # should query database and if name correct, return uuid or smth
    # user = auth.current_user()  # this can be used in handlers, returns the object from verify_password
    from rpgc_server.resources.dbmodels import User
    # FIXME temporary, either move to global or create separate file for auth

    user = User.query.filter(User.username == username and User.password == password)
    return user.id if user else None


@app.route('/', methods=["GET"], defaults={'page': 'index'})
def index(page):
    return "It works!"


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler

    logo = r"""
                _ _______        _
     /\        | |__   __|      | |
    /  \   _ __| | _| | ___  ___| |__
   / /\ \ | '__| |/ / |/ _ \/ __| '_ \
  / ____ \| |  |   <| |  __/ (__| | | |
 /_/    \_\_|  |_|\_\_|\___|\___|_| |_|

                                       """
    log.info(logo)
    log.info('Server starting')

    chats.start()

    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
