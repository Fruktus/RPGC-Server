from os import mkdir
from os.path import join, isdir

import logging as lg
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_monitoringdashboard as dashboard


app = Flask(__name__)
# app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://test:test@localhost/rpgc_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# migrate = Migrate(app, db)


if not isdir('log'):
    mkdir('log')
lg.basicConfig(filename=join('log', 'server.log'),
               format='[{asctime}] {pathname:<20}:{lineno} {levelname:10s} {message}', style='{',
               level=lg.DEBUG)

# app = Flask(__name__)
app.config['SECRET_KEY'] = 'asd'  # SECRET_KEY  # TODO maybe grab from env, will be easier to config
dashboard.config.password = 'asd'  # DASHBOARD_ADMIN_PW
dashboard.bind(app)
