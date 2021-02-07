from os import mkdir, environ
from os.path import isdir

import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_monitoringdashboard as dashboard
from flask_httpauth import HTTPBasicAuth
from flask_sockets import Sockets
import redis

from rpgc_server.resources.wschat import ChatBackend

if not isdir('log'):
    mkdir('log')
logging.basicConfig(  # filename=join('log', 'server.log'),
               format='[{asctime}] {name:<10s}:{lineno:<4d} {levelname:10s} {message}', style='{',
               level=logging.DEBUG)
log = logging.getLogger()


app = Flask(__name__)
# TODO setup proper configuration for all important fields
# app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://test:test@localhost/rpgc_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'asd'  # SECRET_KEY

dashboard.config.password = 'asd'  # DASHBOARD_ADMIN_PW
dashboard.bind(app)

db = SQLAlchemy(app)
auth = HTTPBasicAuth()
sockets = Sockets(app)
chats = ChatBackend()

REDIS_URL = environ['REDIS_URL']
REDIS_CHAN = 'chat'

redis_instance = redis.from_url(REDIS_URL)

# migrate = Migrate(app, db)  # TODO for later maybe
