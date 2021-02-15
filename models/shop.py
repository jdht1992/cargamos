from config import db
from .mixin import BaseModelMixin, BaseModel


class Shop(BaseModel, BaseModelMixin):
    """Class used for shops"""
    __tablename__ = 'shop'

    name = db.Column(db.String(30), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    catalog_id = db.Column(db.Integer, db.ForeignKey('catalog.id'), nullable=False)

    def __repr__(self):
        return self.name

    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            "address_id": self.address_id,
            "catalog_id": self.catalog_id
        }


db.create_all()
db.session.commit()

