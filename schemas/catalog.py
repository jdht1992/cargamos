from config import ma
from marshmallow import Schema, fields
from models.catalog import Catalog


class CatalogSchema(ma.Schema):
    class Meta:
        model = Catalog
        fields = ("name", )
