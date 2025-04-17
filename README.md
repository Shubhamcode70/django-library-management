# Library Management System (Django)

This project is a simple Library Management System built using Django and Django REST Framework. It allows an admin to manage books via REST API and lets students view books via a simple UI.

## Features

- Admin Signup & Login (Token-based)
- CRUD APIs for Books (via Django REST Framework)
- Student view with rendered HTML book list
- MySQL Database Integration

## Tech Stack

- Django
- Django REST Framework
- MySQL
- HTML (for student view)

## Setup Instructions

1. Clone this repository
2. Create a virtual environment and activate it
3. Install dependencies:
   ```bash
   pip install -r requirements.txt

Set up MySQL database and add DB config in settings.py

Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
```
Run the server:
```bash
python manage.py runserver
