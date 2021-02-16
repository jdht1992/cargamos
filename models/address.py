from config import db
from .mixin import BaseModelMixin, BaseModel
from models.shop import Shop


class Address(BaseModel, BaseModelMixin):
    __tablename__ = 'address'

    street = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    state = db.Column(db.String(30), nullable=False)
    country = db.Column(db.String(30), nullable=False)
    name_code = db.Column(db.String(30), nullable=False)
    shop = db.relationship('Shop', lazy="dynamic")

    def __repr__(self):
        return f"{self.id}"
