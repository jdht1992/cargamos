from flask import request
from models.shop import Shop
from models.address import Address
from schemas.shop import ShopSchema
from flask_restful import Resource


ERROR_INSERTING_SHOP = "An error ocurred while inserting shop"
ERROR_INSERTING_ADDRESS = "An error ocurred while inserting address"

class CreateShop(Resource):
    def post(self):
        shop_data = ShopSchema().load(request.json)
        address_data = shop_data.pop("address_id")
        address = Address(**address_data)
        
        try:
            address.save()
        except:
            return { "message": ERROR_INSERTING_ADDRESS }, 500
        
        shop = {
            "name": shop_data.get("name"),
            "address_id": address.id
        }

        shop = Shop(**shop)
        try:
            shop.save()
        except:
            return { "message": ERROR_INSERTING_SHOP }, 500

        return { "id": str(shop.id) }, 201
