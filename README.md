# mexico_postal_codes

A public API Rest for accessing Mexico's postal codes provided by the [Servicio Postal Mexicano](https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx)

# API Url

```
With Pagination
https://api.mhcode.dev/v1/postal_codes


Non-Pagination
https://api.mhcode.dev/v2/postal_codes


Interactive
https://mhcode.dev/#mexico_postal_code
```

## Clone the project

```
git clone https://github.com/marceb1296/mexico_postal_codes.git
```

## ENV

> [!WARNING]
> These environment variables are only valid for production. If not provided, the system will use the normal Django database 'db.sqlite3'.

```
POSTGRES_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=porestgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

## Docker

#### Development

```
cd mexico_postal_code

docker compose -f docker-compose.dev.yaml up -d

docker compose -f docker-compose.dev.yaml exec backend python manage.py migrate

# save postal code data into model
docker compose -f docker-compose.dev.yaml exec backend python manage.py createpostalcodes

```

#### Production

> [!WARNING]
> Production compose use .env variables for db

```
cd mexico_postal_code

docker compose up -d

docker compose -f docker-compose.yaml exec backend python manage.py migrate

# save postal code data into model
docker compose -f docker-compose.yaml exec backend python manage.py createpostalcodes
```

## Non-Docker

> [!WARNING]
> In both cases, Production and Development, the 'SECRET_KEY' from 'docker.compose.yaml' should be copied to a .env file.

#### Development

```
cd mexico_postal_code

pip install -r requirements.txt

python manage.py migrate

# save postal code data into model
python manage.py createpostalcodes

python manage.py runserver 0.0.0.0:8000
```

#### Production

```
cd mexico_postal_code

pip install -r requirements.txt

python manage.py migrate

# save postal code data into model
python manage.py createpostalcodes

gunicorn --bind :8000 backend.wsgi
```

## Test

### Docker

```
cd mexico_postal_code

docker compose -f docker-compose.dev.yaml up -d

docker compose -f docker-compose.dev.yaml exec backend python manage.py test

```

### Non-Docker

```
cd mexico_postal_code

pip install -r requirements.txt

python manage.py test
```
