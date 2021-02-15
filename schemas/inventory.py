from config import ma
from marshmallow import Schema, fields, fields, ValidationError, validates
from models.product import Product


class InvetorySchema(ma.Schema):
    sku = fields.String(required=True)
    quantity = fields.Integer(required=True)
    shop_id = fields.Integer(required=True)

    @validates('sku')
    def validate_sku(self, sku): 
        if Product.query.filter_by(sku=sku).first() is None:
            raise ValidationError('product not registered')
