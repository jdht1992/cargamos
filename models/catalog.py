from config import db
from .mixin import BaseModelMixin, BaseModel


class Catalog(BaseModel, BaseModelMixin):
    __tablename__ = 'catalog'

    name = db.Column(db.String(100), nullable=False)
    shop_id = db.Column(db.Integer, db.ForeignKey('shop.id'), nullable=False)
    products = db.relationship('Product', lazy="dynamic")

    def __repr__(self):
        return f"{self.id}"
