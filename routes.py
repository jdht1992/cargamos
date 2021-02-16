from resource.inventory import CreateInventory, DeleteInventory
from resource.catalog import CreateCatalog
from resource.shop import CreateShop 
from resource.product import CreateProduct 

def routes(api):
    api.add_resource(CreateShop, '/api/v1/shop/')
    api.add_resource(CreateCatalog, '/api/v1/catalog/')
    api.add_resource(CreateProduct, '/api/v1/product/')
    api.add_resource(CreateInventory, '/api/v1/inventory/')
    api.add_resource(DeleteInventory, '/api/v1/delete-inventory/')
