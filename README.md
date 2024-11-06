# UrbanoInfoTech

UrbanoInfoTech is a Django-based project that provides user authentication functionalities including signup, login, and email verification.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

## Features

- User signup with email and password
- Email verification for new users
- User login with token-based authentication
- Comprehensive unit tests

## Requirements

- Python 3.12
- Django 5.1.3
- PostgreSQL

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/UrbanoInfoTech.git
    cd UrbanoInfoTech
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv urbano
    source urbano/Scripts/activate  # On Windows
    # source urbano/bin/activate  # On macOS/Linux
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Set up the PostgreSQL database and update the `.env` file with your database credentials:

    ```properties
    SECRET_KEY=your-secret-key
    DEBUG=True
    DATABASE_NAME=urbano
    DATABASE_USER=postgres
    DATABASE_PASSWORD=your-password
    DATABASE_HOST=localhost
    DATABASE_PORT=5432
    EMAIL_HOST_USER=your-email@example.com
    EMAIL_HOST_PASSWORD=your-email-password
    ```

5. Apply the database migrations:

    ```sh
    python manage.py migrate
    ```

6. Create a superuser:

    ```sh
    python manage.py createsuperuser
    ```

7. Start the development server:

    ```sh
    python manage.py runserver
    ```

## Usage

- Access the admin panel at `http://127.0.0.1:8000/admin/`
- Use the API endpoints for user authentication:
  - Signup: `POST /Authentication/signup/`
  - Login: `POST /Authentication/login/`
  - Email verification: `GET /Authentication/activate/<uidb64>/<token>/`

## Running Tests

To run the tests, use the following command:

```sh
python manage.py test
