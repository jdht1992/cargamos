from flask import Flask, request, jsonify, Response
from models.product import Product
from models.inventory import Inventory
from schemas.product import ProductSchema
from flask_restful import Resource
from config import app
from flask_marshmallow import Marshmallow


ma = Marshmallow(app)


class CreateProduct(Resource):
    def post(self):
        product_schema = ProductSchema().load(request.json)
        quantity = product_schema.pop("quantity")
        shop_id = product_schema.pop("shop_id")
        product = Product(**product_schema)
        product.save()
        inventory_data = {
            "product_id": product.id,
            "quantity": quantity,
            "shop_id": shop_id
        }
        inventory = Inventory(**inventory_data)
        inventory.save()
        return { "product": True }, 201
