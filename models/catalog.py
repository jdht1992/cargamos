from config import db
from .mixin import BaseModelMixin, BaseModel


class Catalog(BaseModel, BaseModelMixin):
    __tablename__ = 'catalog'

    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"{self.id}"
