"""contains classes with REST handlers for data units"""
from flask_restful import Resource
from rpgc_server.resources.data_units import User, Room, Message, Preset


# sample handler
class UserHandler(Resource):
    def get(self):
        pass

    def put(self):
        pass

    def post(self):  # one of those unnecessary i think
        pass

    def delete(self):
        pass
