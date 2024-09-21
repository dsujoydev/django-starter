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

## -- Api Design Basic --

### Get all method

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
