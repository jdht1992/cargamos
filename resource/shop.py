from flask import Flask, request, jsonify, Response
from models.shop import Shop
from models.address import Address
from schemas.shop import ShopSchema
from flask_restful import Resource
from config import app
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class CreateShop(Resource):
    def post(self):
        response = ShopSchema().load(request.json)
        address_id = response.get("address_id")
        address = Address(**address_id)
        address.save()
        shop_data = {
            "name": response.get("name"),
            "catalog_id": response.get("catalog_id"),
            "address_id": address.id
        }
        shop = Shop(**shop_data)
        shop.save()
        return { "shop": True }, 201


class ListShop(Resource):
    def get(self):
        all_store = Shop.query.all()
        return { "store": [s.serialize() for s in all_store] }, 200
