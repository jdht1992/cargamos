from flask import Flask, request, jsonify, Response
from models.catalog import Catalog
from schemas.catalog import CatalogSchema
from flask_restful import Resource
from config import app
from flask_marshmallow import Marshmallow


ma = Marshmallow(app)


class CreateCatalog(Resource):
    def post(self):
        response = CatalogSchema().load(request.json)
        catalog = Catalog(**response)
        catalog.save()
        # return { "catalog": True }, 201
        return {'id': str(catalog.id)}, 201
