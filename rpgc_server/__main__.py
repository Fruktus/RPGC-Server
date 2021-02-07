import gevent
from geventwebsocket import WebSocketError

from rpgc_server import app, log, auth, sockets, redis_instance, REDIS_CHAN
from rpgc_server.handlers.messagehandler import MessageHandler
from rpgc_server.handlers.roomhandler import RoomHandler
from rpgc_server.handlers.userhandler import UserHandler
from rpgc_server.handlers.presethandler import PresetHandler
from rpgc_server.resources.wschat import ChatBackend


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


@sockets.route('/echo')
def echo_socket(ws):
    try:
        while not ws.closed:
            message = ws.receive()
            ws.send(message)
    except WebSocketError:
        pass


@sockets.route('/submit')
def inbox(ws):
    """Receives incoming chat messages, inserts them into Redis."""
    while not ws.closed:
        # Sleep to prevent *contstant* context-switches.
        gevent.sleep(0.1)
        message = ws.receive()

        if message:
            app.logger.info(u'Inserting message: {}'.format(message))
            redis_instance.publish(REDIS_CHAN, message)


@sockets.route('/receive')
def outbox(ws):
    """Sends outgoing chat messages, via `ChatBackend`."""
    chats.register(ws)

    while not ws.closed:
        # Context switch while `ChatBackend.start` is running in the background.
        gevent.sleep(0.1)


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

    chats = ChatBackend()
    chats.start()

    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
