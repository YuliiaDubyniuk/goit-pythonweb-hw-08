# Contacts API

REST API для керування контактами, створений за допомогою **FastAPI**, **SQLAlchemy ORM** та **PostgreSQL**.

## Technologies

- Python 3.13
- FastAPI
- SQLAlchemy ORM
- PostgreSQL
- Pydantic
- Alembic
- Poetry
- Docker / Docker Compose
- Swagger UI

## Project Structure

```text
goit-pythonweb-hw-08/
├── alembic/
├── api/
│   └── contacts.py
├── database/
│   ├── db.py
│   └── models.py
├── schemas/
│   └── contact.py
├── config.py
├── main.py
├── alembic.ini
├── docker-compose.yml
├── pyproject.toml
├── poetry.lock
└── README.md
```

## Features

The API supports:

- Create a contact
- Get all contacts
- Get a contact by ID
- Update a contact
- Delete a contact
- Search contacts by first name
- Search contacts by last name
- Search contacts by email
- Get contacts with upcoming birthdays
- Validate request data using Pydantic
- Interactive API documentation with Swagger UI

## Contact Fields

Each contact contains the following fields:

| Field             | Type             | Description                     |
| ----------------- | ---------------- | ------------------------------- |
| `id`              | `integer`        | Unique contact identifier       |
| `first_name`      | `string`         | Contact's first name            |
| `last_name`       | `string`         | Contact's last name             |
| `email`           | `string`         | Contact's email address         |
| `phone`           | `string`         | Contact's phone number          |
| `birth_date`      | `date`           | Contact's date of birth         |
| `additional_data` | `string \| null` | Optional additional information |

## Installation

### 1. Clone the repository

```bash
git clone <https://github.com/YuliiaDubyniuk/goit-pythonweb-hw-08.git>
cd goit-pythonweb-hw-08
```

### 2. Install dependencies

The project uses Poetry for dependency management.

```bash
poetry install
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql+psycopg://postgres:567234@localhost:5432/contacts
```

### 4. Start PostgreSQL

PostgreSQL runs in Docker.

```bash
docker compose up -d
```

Check that the container is running:

```bash
docker ps
```

### 5. Apply database migrations

```bash
poetry run alembic upgrade head
```

## Running the Application

Start the FastAPI server:

```bash
poetry run uvicorn main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

Swagger UI can be used to test all API endpoints directly from the browser.

## API Endpoints

### Create a Contact

```http
POST /contacts/
```

Creates a new contact.

Example request:

```json
{
  "first_name": "Anna",
  "last_name": "Smith",
  "email": "anna.smith@gmail.com",
  "phone": "+380501112233",
  "birth_date": "1995-03-15",
  "additional_data": "Friend"
}
```

### Get All Contacts

```http
GET /contacts/
```

Returns a list of all contacts.

### Search Contacts

Contacts can be filtered using query parameters.

#### Search by first name

```http
GET /contacts/?first_name=Anna
```

#### Search by last name

```http
GET /contacts/?last_name=Smith
```

#### Search by email

```http
GET /contacts/?email=anna.smith@gmail.com
```

First name and last name searches support partial and case-insensitive matching.

Email search uses an exact match.

### Get Contact by ID

```http
GET /contacts/{contact_id}
```

Example:

```http
GET /contacts/1
```

### Update a Contact

```http
PUT /contacts/{contact_id}
```

Updates an existing contact.

### Delete a Contact

```http
DELETE /contacts/{contact_id}
```

Deletes an existing contact.

### Upcoming Birthdays

```http
GET /contacts/birthdays
```

Returns contacts whose birthdays are within the next 7 days.

## Database Migrations

Alembic is used to manage database schema migrations.

### Create a migration

After changing SQLAlchemy models:

```bash
poetry run alembic revision --autogenerate -m "describe changes"
```

### Apply migrations

```bash
poetry run alembic upgrade head
```

## Validation

Request data is validated using **Pydantic**.

The API validates:

- required fields;
- email format;
- birth date format;
- data types;
- optional fields.

Email addresses are normalized to lowercase.

Invalid request data results in a validation error returned by FastAPI.

## Stopping the Application

Stop the FastAPI server with:

```text
Ctrl+C
```

Stop the PostgreSQL container with:

```bash
docker compose down
```

The PostgreSQL data is stored in a Docker volume and is preserved when the container is stopped.
