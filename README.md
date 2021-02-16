## Cargamos Demo
Crear una API Rest con Flask que implemente un sistema de inventario de productos

### Requerimientos
 - Python 3.8
 - Virtualenv
 - Postgresql
 

 ### Installation

Clonación del proyecto
```sh
git clone https://github.com/jdht1992/cargamos.git
```

Crear y activar virtualenv.
```sh
python3 -m venv env_cargamos
source env_cargamos/bin/activate
```
Instalacion de paquetes.
```
cd cargamos
pip install -r requirements.txt
```

### Ejecutar proyecto .

Se corre el proyecto.
```sh

```




### Módulos incluidos
- 1.- API en donde se pueda crear la tienta

endpoint 
 ```sh
/api/v1/shop/
```
PayLoad
 ```sh
{
    "name": "cargamos",
    "address_id":
        {
            "street": "Andador mayapan",
            "city": "Zapopan",
            "state": "Jalisco",
            "country": "Mexico",
            "name_code": "97159"
        }
}
```

- 2.- API en donde se pueda crear catalogo.

endpoint 
 ```sh
/api/v1/catalog/
```
PayLoad
 ```sh
{
    "name": "catalogo",
    "shop_id": 1
}
```

- 3.- API en donde se pueda crear el producto

endpoint 
 ```sh
/api/v1/product/
```
PayLoad
 ```sh
{
    "title": "Product1",
    "description": "un articulo de ropa",
    "price": 35.2,
    "is_featured": true,
    "sku": "abc1234",
    "catalog_id": 3,
    "quantity": 5,
    "shop_id": 1
}
```

- 4.- API en donde se pueda agregar inventario

endpoint 
 ```sh
/api/v1/inventory/
```
PayLoad
 ```sh
{
    "sku": "abc1234",
    "quantity": 10,
    "shop_id": 1 
}
```

- 5.- API en donde se pueda quitar inventario

endpoint 
 ```sh
/api/v1/delete-inventory/
```
PayLoad
 ```sh
{
    "sku": "abc1234",
    "quantity": 10,
    "shop_id": 1 
}
```

