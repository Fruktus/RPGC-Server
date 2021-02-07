import gevent
from geventwebsocket import WebSocketError

from rpgc_server import sockets, app, redis_instance, REDIS_CHAN, chats


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
