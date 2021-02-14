from flask import Flask, request, jsonify, Response
from models.shops import Shop, Address, Product, Inventory, Catalog
from flask_restful import Resource
from config import app
from flask_marshmallow import Marshmallow
from marshmallow import fields, ValidationError, validates


ma = Marshmallow(app)


class CatalogSchema(ma.Schema):
    class Meta:
        model = Catalog
        fields = ("name", )


class CreateCatalog(Resource):
    def post(self):
        response = CatalogSchema().load(request.json)
        catalog = Catalog(**response)
        catalog.save()
        return { "catalog": True }, 201


class AddressSchema(ma.Schema):
    street = fields.String(required=True)
    city = fields.String(required=True)
    state = fields.String(required=True)
    country = fields.String(required=True)
    name_code = fields.String(required=True)


class ShopSchema(ma.Schema):
    address_id = fields.Nested(AddressSchema)

    class Meta:
        model = Shop
        fields = ("name", "address_id", "catalog_id")


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


class ProductSchema(ma.Schema):
    title = fields.String(required=True)
    description = fields.String(required=True)
    price = fields.Float(required=True)
    is_featured = fields.Boolean(required=True)
    sku = fields.String(required=True)
    catalog_id = fields.Integer(required=True) 
    quantity = fields.Integer(required=True)
    shop_id = fields.Integer(required=True)



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

class InvetorySchema(ma.Schema):
    sku = fields.String(required=True)
    quantity = fields.Integer(required=True)
    shop_id = fields.Integer(required=True)

    @validates('sku')
    def validate_sku(self, sku): 
        if Product.query.filter_by(sku=sku).first() is None:
            raise ValidationError('product not registered')


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
