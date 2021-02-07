from marshmallow import fields, Schema


# how to validate condition "at least one required (other than id):
# https://marshmallow.readthedocs.io/en/latest/api_reference.html#marshmallow.decorators.validates_schema


# INFO: those schemas are for validating user-submitted responses, database will return different ones
# FIXME: Circular dependency
class UserGetSchema(Schema):
    id = fields.UUID(required=True)
    # username = fields.Str()
    # email = fields.Email()
    # created_at = fields.DateTime(dump_only=True)
    # room_owned = fields.Nested(RoomSchema, many=True)  # TODO: return the array or not? force client to ask?


class UserPostSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    email = fields.Email(required=True)


class UserPutSchema(Schema):
    id = fields.UUID(required=True)  # you must supply uuid for the user you wish to modify
    # TODO ^ obtained from auth, possibly unnecessary
    username = fields.Str()
    password = fields.Str(load_only=True)
    email = fields.Email()


class UserDeleteSchema(Schema):
    id = fields.UUID(required=True)


class RoomGetSchema(Schema):
    id = fields.UUID(required=True)
    owner_id = fields.Nested(UserGetSchema)  # TODO: just return uuid, not full nested user
    # owner = relationship('User', back_populates='rooms_owned')  # IDK why there is two of them
    name = fields.Str()
    visible = fields.Boolean()
    password = fields.Str()


class RoomPostSchema(Schema):
    owner_id = fields.UUID(required=True)  # TODO: just return uuid, not full nested user
    # owner = relationship('User', back_populates='rooms_owned')  # IDK why there is two of them
    name = fields.Str(required=True)
    visible = fields.Boolean(required=True)
    password = fields.Str()  # may be empty, no password then


class RoomPutSchema(Schema):
    id = fields.UUID(required=True)
    owner_id = fields.Nested(UserGetSchema)  # TODO: just return uuid, not full nested user
    # owner = relationship('User', back_populates='rooms_owned')  # IDK why there is two of them
    name = fields.Str()
    visible = fields.Boolean()
    password = fields.Str()  # may be empty, no password then


class RoomDeleteSchema(Schema):
    id = fields.UUID(required=True)


class MessageGetSchema(Schema):
    room_id = fields.UUID(required=True)
    id = fields.Integer(required=True)


class MessagePostSchema(Schema):
    room_id = fields.UUID(required=True)
    author = fields.Nested(UserGetSchema, required=True)  # TODO: replace with uuid
    data = fields.Str(required=True)

# no MessagePutSchema, you cant edit messages # TODO: or should i allow it?


class MessageDeleteSchema(Schema):
    room_id = fields.UUID(required=True)
    id = fields.Integer(required=True)


# TODO: this one needs bit more thought in the models first
# class PresetGetSchema(Schema):
#
#
# class Preset(Base):
#     # info: this one is for users only, cannot be used directly in message as formatting, you need to use data
#     __tablename__ = 'presets'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(64))
#     # user = Column(UUID(as_uuid=True), ForeignKey('users.id'))
#     user = Column(Integer, ForeignKey('users.id'))
#     data = Column(String)
