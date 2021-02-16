from flask import request
from models.product import Product
from models.inventory import Inventory
from schemas.product import ProductSchema
from flask_restful import Resource


ERROR_INSERTING_PRODUCT = "An error ocurred while inserting product"
ERROR_INSERTING_INVENTORY = "An error ocurred while inserting inventory"

class CreateProduct(Resource):
    def post(self):
        product_data = ProductSchema().load(request.json)
        quantity = product_data.pop("quantity", None)
        shop_id = product_data.pop("shop_id", None)
        product = Product(**product_data)

        try:
            product.save()
        except:
            return { "message": ERROR_INSERTING_PRODUCT }, 500
        
        inventory_data = {
            "product_id": product.id,
            "quantity": quantity,
            "shop_id": shop_id
        }
        
        inventory = Inventory(**inventory_data)

        try:
            inventory.save()
        except:
            return { "message": ERROR_INSERTING_INVENTORY }, 500
        
        return { "id": str(product.id) }, 201
