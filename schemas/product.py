from config import ma
from marshmallow import Schema, fields

class ProductSchema(ma.Schema):
    title = fields.String(required=True)
    description = fields.String(required=True)
    price = fields.Float(required=True)
    is_featured = fields.Boolean(required=True)
    sku = fields.String(required=True)
    catalog_id = fields.Integer(required=True) 
    quantity = fields.Integer(required=True)
    shop_id = fields.Integer(required=True)