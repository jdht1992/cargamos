import unittest
import json

from app import app
from config import db

from models.shop import Shop
from models.address import Address


class CatalogTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        db.create_all()

    def test_successful_catalog(self):
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

        # Given
        payload = json.dumps({
            "name": "prueba",
            "shop_id": shop.id
        })

        # When
        response = self.app.post(
            '/api/v1/catalog/', 
            headers={"Content-Type": "application/json"}, 
            data=payload
            )

        # Then
        self.assertEqual(dict, type(response.json))
        self.assertEqual(201, response.status_code)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
