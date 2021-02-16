from config import db
from .mixin import BaseModelMixin, BaseModel


class Inventory(BaseModel, BaseModelMixin):
    __tablename__ = "inventory"

    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False, unique=True)
    quantity = db.Column(db.Integer, nullable=False)
    shop_id = db.Column(db.Integer, db.ForeignKey('shop.id'), nullable=False)

    def __repr__(self):
        return f"{self.product_id}"
