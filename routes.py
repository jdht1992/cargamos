from views import CreateShop, ListShop, CreateProduct, CreateCatalog, CreateInventory

def routes(api):
    api.add_resource(CreateCatalog, '/api/create-catalog/')
    api.add_resource(CreateShop, '/api/ceate-shop/')
    api.add_resource(ListShop, '/api/list-shop/')
    api.add_resource(CreateProduct, '/api/create-product/')
    api.add_resource(CreateInventory, '/api/create-inventory/')
