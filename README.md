# Django File Transfer API

## Overview
This is a Django-based API project for managing file ownership transfers and revocations. The project provides a robust system for transferring and revoking file ownership between users with secure authentication.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation-instructions)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication-for-api-usage)
- [Contributing](#contributing)
- [License](#license)

## Requirements
Before you begin, ensure you have the following installed:
- Python 3.x
- MySQL Database
- pip (Python package manager)
- Virtual Environment (`venv`)

## Installation Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/django-file-transfer-api.git
cd django-file-transfer-api
```

### 2. Set Up a Virtual Environment
Create and activate a virtual environment:
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment (Unix/macOS)
source venv/bin/activate

# Activate virtual environment (Windows)
venv\Scripts\activate
```

### 3. Install Dependencies
Install all required dependencies from `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Configure MySQL Database
1. Ensure MySQL is installed and running.
2. Create a new MySQL database:
```sql
CREATE DATABASE your_database_name;
```

3. Update `iudx_wsl/settings.py` with your MySQL credentials:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Run Migrations
Set up the database schema:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Initial Users
To create users, use the Django shell:
```bash
python manage.py shell
```
In the shell, run the user creation script provided in the installation instructions.
```bash
from django.contrib.auth.models import User

# List of users to create in bulk
users = [
    {'username': 'alice', 'email': 'alice@example.com', 'password': 'password123'},
    {'username': 'bob', 'email': 'bob@example.com', 'password': 'password123'},
    {'username': 'charlie', 'email': 'charlie@example.com', 'password': 'password123'},
    {'username': 'david', 'email': 'david@example.com', 'password': 'password123'},
]

# Loop through and create users if they don't already exist
for user_data in users:
    if not User.objects.filter(username=user_data['username']).exists():
        User.objects.create_user(username=user_data['username'], email=user_data['email'], password=user_data['password'])
        print(f"User '{user_data['username']}' created successfully!")
    else:
        print(f"User '{user_data['username']}' already exists.")
```

### 7. Run the Server
Start the development server:
```bash
python manage.py runserver
```
The project will be available at: **http://127.0.0.1:8000/**

## API Endpoints

### 1. Transfer File
- **URL**: `/api/transfer/`
- **Method**: `POST`
- **Request Body**:
```json
{
    "file_id": 1,
    "to_user_id": 2
}
```

### 2. Revoke File Transfer
- **URL**: `/api/revoke/`
- **Method**: `POST`
- **Request Body**:
```json
{
    "file_id": 1
}
```

## Authentication for API Usage
To use the APIs, you must be authenticated.

### Available 
```
User ID  Username  Password   
---      -------   ---------
1        alice     password123
2        bob       password123  
3        charlie   password123
4        david     password123
```
### Authentication Steps
1. In your API client (e.g., Postman), go to the **Authentication** tab.
2. Select **Basic Auth**
3. Provide the username and password for one of the users listed above.

Example:
- **Username**: `alice`
- **Password**: `password123`