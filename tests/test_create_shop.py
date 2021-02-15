import unittest
import json

from app import app
from config import db


class ShopTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        # self.db = db.get_db()

    def test_successful_shop(self):
        # Given
        payload = json.dumps({
            "name": "exameple10",
            "address_id":
                {
                    "street": "primera",
                    "city": "segunda",
                    "state": "tercero",
                    "country": "cuarto",
                    "name_code": "123abc"
                },
            "catalog_id": 1
        })

        # When
        response = self.app.post(
            '/api/ceate-shop/', 
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
