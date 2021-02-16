from flask import request
from models.catalog import Catalog
from schemas.catalog import CatalogSchema
from flask_restful import Resource


ERROR_INSERTING = "An error ocurred while inserting catalog"


class CreateCatalog(Resource):
    def post(self):
        catalog_data = CatalogSchema().load(request.json)
        catalog = Catalog(**catalog_data)
        try:
            catalog.save()
        except:
            return { "message": ERROR_INSERTING }, 500
        return { 'id': str(catalog.id) }, 201
