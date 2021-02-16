from config import ma
from marshmallow import fields, ValidationError, validates
from models.product import Product
from models.inventory import Inventory


class InvetorySchema(ma.Schema):
    # sku = fields.String(required=True)
    # quantity = fields.Integer(required=True)
    # shop_id = fields.Integer(required=True)

    # @validates('sku')
    # def validate_sku(self, sku): 
    #     if Product.query.filter_by(sku=sku).first() is None:
    #         raise ValidationError('product not registered')
    class Meta:
        model = Inventory
        fields = ("sku", "quantity", "shop_id")
