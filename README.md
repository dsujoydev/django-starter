# -- Django Project Init -- Api Design Basic

## -- Django Project Init --

1. Create a directory on your local environment (macOS)
2. Create a virtual environment with python

```javascript
python3 -m venv venv
```

3. Activate the virtual environment

```javascript
source venv/bin/activate
```

4. Install Django in the directory

```javascript
python3 -m pip install Django
```

5. Django version check

```javascript
django-admin --version
```

6. venv dependency check

```javascript
pip freeze > requirements.txt
```

7. Create a project under main directory

```javascript
django-admin startproject folder_name
```

8. Change Directory

```javascript
cd folder_name
```

9. Run server

```javascript
python3 manage.py runserver
```

10. Create new app under it

```javascript
python3 manage.py startapp products
```

11.

## -- Api Design Basic --

### Get all method (ex: Products)

- **Method**: GET
- **Endpoint**: `api/v1/products`
- **Authentication**: Basic or Bearer Token
- **Request Body**: None
- **Response Body** :

```javascript
id: id,
name: name,
..............
```

- **Response Code**:
  - _200_ : OK
  - _401_: Unauthorized
  - _500_: Server Error

### Post method (ex: Products)

- **Method**: Post
- **Endpoint**: `api/v1/products`
- **Authentication**: Basic or Bearer Token
- **Request Body/Payload**:

```javascript
id: id,
name: name,
price: price,
quantity: qty,
..............
```

- **Response Code**:
  - _200_ : OK --> Created
  - _400_ : Bad request
  - _401_ : Unauthorized
  - _500_ : Server Error

### Get one method (ex: Product)

- **Method**: GET
- **Endpoint**: `api/v1/products/{id}`
- **Authentication**: Basic or Bearer Token
- **Request Body**: None
- **Response Body** :

```javascript
id: 5 (ex.),
name: name,
price: price,
..............
```

- **Response Code**:
  - _200_ : OK
  - _401_: Unauthorized
  - _500_: Server Error
  - _404_: Not Found

### Put method (ex: Product)

- **Method**: Put
- **Endpoint**: `api/v1/products/{id}`
- **Authentication**: Basic or Bearer Token
- **Request Body/Payload**: _PUT_ --> Full Object, _Patch_ --> Partial Object

```javascript
name: name,
price: price,
quantity: qty,
..............
```

or

```javascript
name: name,
..............
```

- **Response Body** : Updated Object
- **Response Code**:
  - _200_ : OK --> Updated
  - _400_ : Bad request
  - _401_ : Unauthorized
  - _404_ : Not Found
  - _500_ : Server Error

### Delete method (ex: Product)

- **Method**: Delete
- **Endpoint**: `api/v1/products/{id}`
- **Authentication**: Basic or Bearer Token
- **Request Body**: None
- **Response Code**:
  - _200_ : OK --> Deleted
  - _401_ : Unauthorized
  - _404_ : Not Found
  - _500_ : Server Error
