from config import ma
from marshmallow import fields, ValidationError, validates
from models.product import Product
from models.inventory import Inventory


class InvetorySchema(ma.Schema):
    class Meta:
        model = Inventory
        fields = ("sku", "quantity", "shop_id")
