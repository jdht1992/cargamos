from config import ma
from marshmallow import Schema, fields


class AddressSchema(ma.Schema):
    street = fields.String(required=True)
    city = fields.String(required=True)
    state = fields.String(required=True)
    country = fields.String(required=True)
    name_code = fields.String(required=True)
