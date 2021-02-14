from config import db


class BaseModelMixin:
    def save(self):
        """This methos create a row with the obj data"""
        db.session.add(self)
        db.session.commit()
        return self.id


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())


class Shop(BaseModel, BaseModelMixin):
    """Class used for shops"""
    __tablename__ = 'shop'

    name = db.Column(db.String(30))
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


class Catalog(BaseModel, BaseModelMixin):
    __tablename__ = 'catalog'

    name = db.Column(db.String(100))

    def __repr__(self):
        return f"{self.id}"


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


class Inventory(BaseModel, BaseModelMixin):
    __tablename__ = "inventory"

    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Float)
    shop_id = db.Column(db.Integer, db.ForeignKey('shop.id'), nullable=False)

    def __repr__(self):
        return f"{self.title}"

    def serialize(self):
        return {
            "product_id": self.product_id,
            "quantity": self.quantity
        }


db.create_all()
db.session.commit()

