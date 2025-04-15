# Planner API

Planner is a project and task management API built with Django and Django REST Framework.

## Features

- User registration and authentication (JWT)
- Admin-only user listing
- Project creation, listing, updating, and deletion
- Task creation, assignment to projects, update, delete
- View and update user profile
- API documentation with Swagger UI

## Tech Stack

- Python 3.8+
- Django 3.2+
- Django REST Framework
- djangorestframework-simplejwt
- drf-spectacular (for API documentation)
- PostgreSQL or SQLite (default)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/planner_backend.git
cd planner_backend
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

### 7. Access the API

- Admin panel: http://localhost:8000/admin/
- API documentation (Swagger): http://localhost:8000/api/schema/swagger-ui/
- API documentation (ReDoc): http://localhost:8000/api/schema/redoc/

## Running Tests

```bash
python manage.py test
```

## Author

Fatemeh – Backend Developer