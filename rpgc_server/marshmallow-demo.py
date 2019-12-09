from marshmallow import fields, Schema, ValidationError


class UserSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    created_at = fields.DateTime()


user_schema = UserSchema()
try:
    user = UserSchema().load({"name": "Ronnie", "email": "invalid"})
except ValidationError as err:
    print(err.messages)
    print(err.valid_data)

print(UserSchema().validate({"name": "Ronnie", "email": "asd@asd.com"}))
print(UserSchema().validate({"name": "Ronnie"}))
print(UserSchema().validate({"name": "Ronnie", "email": "invalid-email"}))

# json_res = schema.dumps()
# from_json = schema.loads(json)
