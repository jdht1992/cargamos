from config import db
from .mixin import BaseModelMixin, BaseModel


class Address(BaseModel, BaseModelMixin):
    __tablename__ = 'address'

    street = db.Column(db.String(100))
    city = db.Column(db.String(30))
    state = db.Column(db.String(30))
    country = db.Column(db.String(30))
    name_code = db.Column(db.String(30))

    def __repr__(self):
        return self.street

    def serialize(self):
        return {
            'id': self.id, 
            'street': self.street,
            'city': self.city,
        }
