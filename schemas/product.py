from config import ma
from marshmallow import fields
from models.product import Product


class ProductSchema(ma.Schema):
    quantity = fields.Integer(required=True)
    shop_id = fields.Integer(required=True)
    
    class Meta:
        model = Product
        fields = ("title", "description", "price", "is_featured", "sku", "catalog_id", "quantity", "shop_id")
