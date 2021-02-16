import unittest
import json

from app import app
from config import db


class ShopTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        db.create_all()

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
                }
        })

        # When
        response = self.app.post(
            '/api/v1/shop/', 
            headers={"Content-Type": "application/json"}, 
            data=payload
            )

        # Then
        self.assertEqual(dict, type(response.json))
        self.assertEqual(201, response.status_code)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
