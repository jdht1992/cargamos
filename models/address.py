from config import db
from .mixin import BaseModelMixin, BaseModel


class Address(BaseModel, BaseModelMixin):
    __tablename__ = 'address'

    street = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    state = db.Column(db.String(30), nullable=False)
    country = db.Column(db.String(30), nullable=False)
    name_code = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return self.street
