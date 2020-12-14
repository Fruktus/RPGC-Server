from os import mkdir
from os.path import join, isdir

import logging as lg
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_monitoringdashboard as dashboard
from flask_httpauth import HTTPBasicAuth
from flask_socketio import SocketIO


if not isdir('log'):
    mkdir('log')
lg.basicConfig( # filename=join('log', 'server.log'),
               format='[{asctime}] {pathname:<20}:{lineno} {levelname:10s} {message}', style='{',
               level=lg.DEBUG)


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
socketio = SocketIO()

# migrate = Migrate(app, db)  # TODO for later maybe

# TODO to build app
# def create_app(debug=False):
#     """Create an application."""
#     app = Flask(__name__)
#     app.debug = debug
#     app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'
#
#     from .main import main as main_blueprint
#     app.register_blueprint(main_blueprint)
#
#     socketio.init_app(app)
#     return app
