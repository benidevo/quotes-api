# Quotes API 

A REST API for posting and retrieving quotes. Clients wil be able to communicate with this Web API from 2 endpoints:
api/quotes/ - accepts GET and POST methods, allowing only an admin user to create new instances and all users to retrieve a list with all the available quotes. 

api/quotes/<id>/ - accepts GET and PATCH and DELETE methods, allowing a user to retrieve, update or delete an object instance. However, only an admin user can use the PATCH and DELETE methods.

## Technologies 

The following technologies were used in this project:

- [Python](https://www.python.org/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [SQLite3](https://www.sqlite.org/index.html)

## Requirements

Before starting, you need to have [Git](https://git-scm.com) and [Python 3.9](https://www.python.org/)installed. Alternatively, you can download the code as a zip file

## Clone this project

    git clone https://github.com/benidevo/quotes-api.git

## Create virtual environment

    python3 -m venv env

## Activate virtual environment

    . env/bin/activate

## Install dependencies

    pip install -r requirements.txt

## Make migrations

    python manage.py makemigrations

## Migrate apps and database

    python manage.py migrate

## Create an admin user profile

    python manage.py createsuperuser

## Start server

    python manage.py runserver


# Endpoints

The endpoints and responses are described below.

## Get list of Quotes

### Request

`GET api/quotes/`

    curl -i -H 'Accept: application/json' http://localhost:8000/api/jobs

### Response

    {
        "message": "success",
        "data": {
            "quotes": [
                {
                    "id": <UUID>
                    "quote_author": <string>,
                    "quote_body": <string>,
                    "context": <string>,
                    "source": <string>
                },
                {
                    "id": <UUID>
                    "quote_author": <string>,
                    "quote_body": <string>,
                    "context": <string>,
                    "source": <string>
                }
            ]
        },
        "errors": null
    }

## Create a new quote

### Request

`POST api/quotes/`

    curl -i -H 'Accept: application/json' -d 'name=Foo&status=new' http://localhost:8000/api/s

### Response

    {
        "message": "success",
        "data": {
            "quotes": {
                "id": <UUID>
                "quote_author": <string>,
                "quote_body": <string>,
                "context": <string>,
                "source": <string>
            }
        },
        "errors": null
    }

## Get a quote by ID

### Request

`GET api/quotes/<id>`

    curl -i -H 'Accept: application/json' http://localhost:8000/jobs/<id>

### Response

    {
        "message": "success",
        "data": {
            "quotes": {
                "id": <UUID>
                "quote_author": <string>,
                "quote_body": <string>,
                "context": <string>,
                "source": <string>
            }
        },
        "errors": null
    }

## Update a job offer

### Request

`PATCH api/quotes/<id>`

    curl -i -H 'Accept: application/json' http://localhost:8000/jobs/<id>

### Response

      {
        "message": "success",
        "data": {
            "quotes": {
                "id": <UUID>
                "quote_author": <string>,
                "quote_body": <string>,
                "context": <string>,
                "source": <string>
            }
        },
        "errors": null
    }   "errors": null
    }

## Delete a quote

### Request

`DELETE api/quotes/api`

    curl -i -H 'Accept: application/json' http://localhost:8000/api/jobs/<id>

### Response

    {
        "message": "success",
        "data": {
            "data": {}
        },
        "errors": null
    }
