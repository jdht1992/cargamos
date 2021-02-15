from config import db
from .mixin import BaseModelMixin, BaseModel


class Inventory(BaseModel, BaseModelMixin):
    __tablename__ = "inventory"

    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    # quantity = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    shop_id = db.Column(db.Integer, db.ForeignKey('shop.id'), nullable=False)

    def __repr__(self):
        return f"{self.title}"

    def serialize(self):
        return {
            "product_id": self.product_id,
            "quantity": self.quantity
        }
