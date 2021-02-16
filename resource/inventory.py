from flask import request
from models.product import Product
from models.inventory import Inventory
from schemas.inventory import InvetorySchema
from flask_restful import Resource
from typing import List


class LowInventory:

    _observers = []


    def attach(self, observer) -> None:
        self._observers.append(observer)

    def detach(self, observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def validar_inventory(self, inventory) -> None:
        manager = ManagerObserver()
        owner = OwnerObserver()
        customer = CustomerObserver()
        if inventory.quantity > 20:
            self.attach(manager)
            self.attach(customer)
        elif inventory.quantity == 0:
            self.attach(owner)
        self.notify()


class ManagerObserver:
    def update(self, subject) -> None:
        print("Make a discount or transfer the products")        


class CustomerObserver:
    def update(self, subject) -> None:
        print("Visit store for probable discountss")        


class OwnerObserver:
    def update(self, subject) -> None:
        print("Order missing product")


class CreateInventory(Resource):
    def post(self):
        low_inventory = LowInventory()
        inventory_data = InvetorySchema().load(request.json)
        
        sku = inventory_data.get("sku")
        quantity = inventory_data.get("quantity")
        shop_id = inventory_data.get("shop_id")

        product = Product.query.filter_by(sku=sku).first()
        inventory = Inventory.query.filter_by(product_id=product.id, shop_id=shop_id).first()
    
        inventory.quantity = inventory.quantity + quantity
        inventory.save()
        low_inventory.validar_inventory(inventory)

        return { "id": str(inventory.id) }, 200


class DeleteInventory(Resource):
    def post(self):
        low_inventory = LowInventory()
        inventory_data = InvetorySchema().load(request.json)

        sku = inventory_data.get("sku")
        quantity = inventory_data.get("quantity")
        shop_id = inventory_data.get("shop_id")
        
        product = Product.query.filter_by(sku=sku).first()
        inventory = Inventory.query.filter_by(product_id=product.id, shop_id=shop_id).first()
        
        inventory.quantity = inventory.quantity - quantity
        inventory.save()
        low_inventory.validar_inventory(inventory)

        return { "id": str(inventory.id) }, 200
