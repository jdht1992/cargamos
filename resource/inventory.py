from flask import Flask, request, jsonify, Response
from models.product import Product
from models.inventory import Inventory
from schemas.inventory import InvetorySchema
from flask_restful import Resource
from config import app
from flask_marshmallow import Marshmallow
from typing import List


ma = Marshmallow(app)


class CreateInventory(Resource):
    def post(self):
        inventory_schema = InvetorySchema().load(request.json)#request.get_json()
        sku = inventory_schema.get("sku")
        quantity = inventory_schema.get("quantity")
        product = Product.query.filter_by(sku=sku).first()
        inventory = Inventory.query.filter_by(product_id=product.id).first()
        new_quantity = inventory.quantity + quantity
        inventory.quantity = new_quantity
        inventory.save()
        return { "inventory": True }, 201


class DeleteInventory(Resource):
    def post(self):
        inventory_schema = InvetorySchema().load(request.json)
        sku = inventory_schema.get("sku")
        quantity = inventory_schema.get("quantity")
        product = Product.query.filter_by(sku=sku).first()
        inventory = Inventory.query.filter_by(product_id=product.id).first()
        new_quantity = inventory.quantity - quantity
        inventory.quantity = new_quantity
        inventory.save()
        if inventory.quantity is None:
            print("notify()")
        return { "inventory": True }, 200
