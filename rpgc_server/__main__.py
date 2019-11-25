from flask import Flask
from rpgc_server import app


if __name__ == '__main__':
    app = Flask(app)
    app.run()
