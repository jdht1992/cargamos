import unittest
import json

from app import app
from config import db

from models.product import Product
from models.address import Address
from models.shop import Shop
from models.catalog import Catalog
from models.inventory import Inventory


class InventoryTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        db.create_all()

    def test_successful_inventory(self):
        address_data = {
            "street": "primera",
            "city": "segunda",
            "state": "tercero",
            "country": "cuarto",
            "name_code": "123abc"
        }
        address = Address(**address_data)
        address.save()

        shop_data = {
            "name": "un ejemplo mas",
            "address_id": address.id
        }
        shop = Shop(**shop_data)
        shop.save()

        catalog_data = {
            "name": "primavera verano",
            "shop_id": shop.id
        }
        catalog = Catalog(**catalog_data)
        catalog.save()

        product_data = {
            "title": "p2",
            "description": "un articulo de ropa",
            "price": 2.2,
            "is_featured": True,
            "sku": "abc12345678",
            "catalog_id": catalog.id,
        }

        product = Product(**product_data)
        product.save()

        inventory_data = {
            "product_id": product.id,
            "quantity": 10,
            "shop_id": shop.id 
        }
        inventory = Inventory(**inventory_data)
        inventory.save()

        # Given
        payload = json.dumps({
            "sku": "abc12345678",
            "quantity": 10,
            "shop_id": shop.id
        })

        # When
        response = self.app.post(
            '/api/v1/inventory/', 
            headers={"Content-Type": "application/json"}, 
            data=payload
            )

        # Then
        self.assertEqual(dict, type(response.json))
        self.assertEqual(200, response.status_code)


    def tearDown(self):
        db.session.remove()
        db.drop_all()
