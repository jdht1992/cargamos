from config import db
from .mixin import BaseModelMixin, BaseModel


class Product(BaseModel, BaseModelMixin):
    __tablename__ = 'product'

    title = db.Column(db.String(30), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    is_featured = db.Column(db.Boolean, default=True)
    sku = db.Column(db.String(50), nullable=False, unique=True)
    catalog_id = db.Column(db.Integer, db.ForeignKey('catalog.id'), nullable=False)
    inventory = db.relationship("Inventory", uselist=False)
    
    def __repr__(self):
        return self.title
