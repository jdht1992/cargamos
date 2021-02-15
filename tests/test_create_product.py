import unittest
import json

from app import app
from config import db


class ProductTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        # self.db = db.get_db()

    def test_successful_product(self):
        # Given
        payload = json.dumps({
            "title": "A15",
            "description": "un articulo de ropa",
            "price": 2.2,
            "is_featured": True,
            "sku": "abc123",
            "catalog_id": 1,
            "quantity": 5,
            "shop_id": 1
        })

        # When
        response = self.app.post(
            '/api/create-product/', 
            headers={"Content-Type": "application/json"}, 
            data=payload
            )

        # Then
        self.assertEqual(dict, type(response.json))
        self.assertEqual(201, response.status_code)

    # def tearDown(self):
    #     # Delete Database collections after the test is complete
    #     for collection in self.db.list_collection_names():
    #         self.db.drop_collection(collection)

    