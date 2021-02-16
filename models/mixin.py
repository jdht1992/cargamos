from config import db


class BaseModelMixin:
    def save(self) -> None:
        """This methos create a row with the obj data"""
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        "This method delete record from the db"
        db.session.delete(self)
        db.session.commit()

class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
