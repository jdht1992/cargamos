from config import ma
from models.address import Address


class AddressSchema(ma.Schema):
    class Meta:
        model = Address
        fields = ("street", "city", "state", "country", "name_code")
