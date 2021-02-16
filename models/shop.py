from config import db
from .mixin import BaseModelMixin, BaseModel


class Shop(BaseModel, BaseModelMixin):
    __tablename__ = 'shop'

    name = db.Column(db.String(30), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    catalogs = db.relationship('Catalog', lazy="dynamic")
    inventories = db.relationship('Inventory', lazy="dynamic")

    def __repr__(self):
        return self.name
