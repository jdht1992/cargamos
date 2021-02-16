from config import ma
from marshmallow import fields
from models.shop import Shop
from schemas.address import AddressSchema


class ShopSchema(ma.Schema):
    address_id = fields.Nested(AddressSchema)

    class Meta:
        model = Shop
        fields = ("name", "address_id",)
