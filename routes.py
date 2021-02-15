from resource.inventory import CreateInventory, DeleteInventory
from resource.catalog import CreateCatalog
from resource.shop import CreateShop, ListShop 
from resource.product import CreateProduct 

def routes(api):
    api.add_resource(CreateCatalog, '/api/create-catalog/')
    api.add_resource(CreateShop, '/api/ceate-shop/')
    api.add_resource(ListShop, '/api/list-shop/')
    api.add_resource(CreateProduct, '/api/create-product/')
    api.add_resource(CreateInventory, '/api/create-inventory/')
    api.add_resource(DeleteInventory, '/api/delete-inventory/')
