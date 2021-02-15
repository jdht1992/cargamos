from config import db
from .mixin import BaseModelMixin, BaseModel


class Product(BaseModel, BaseModelMixin):
    __tablename__ = 'product'

    title = db.Column(db.String(30))
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    is_featured = db.Column(db.Boolean, default=True)
    sku = db.Column(db.String(50))#unique = True, nullable = False
    catalog_id = db.Column(db.Integer, db.ForeignKey('catalog.id'), nullable=False)
    

    def __repr__(self):
        return self.title

    def serialize(self):
        return {
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "is_featured": self.is_featured,
            "sku": self.sku
        }
