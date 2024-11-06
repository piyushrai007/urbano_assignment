# UrbanoInfoTech

UrbanoInfoTech is a Django-based project that provides user authentication functionalities including signup, login, and email verification.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Testing the API on the Hosted Server](#testing-the-api-on-the-hosted-server)
- [Running Tests Locally](#running-tests-locally)
- [Environment Variables](#environment-variables)


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

## Testing the API on the Hosted Server

You can also test the API endpoints directly on the hosted server:

- **Base URL**: `https://piyushraivds45.pythonanywhere.com`
- **API Endpoints**:
  - **Signup**: `POST https://piyushraivds45.pythonanywhere.com/Authentication/signup/`
    - Use JSON payload with user details, such as:
      ```json
      {
        "username": "testuser",
        "email": "test@example.com",
        "password": "yourpassword"
      }
      ```
  - **Login**: `POST https://piyushraivds45.pythonanywhere.com/Authentication/login/`
    - Use JSON payload with login credentials, such as:
      ```json
      {
        "username": "testuser",
        "password": "yourpassword"
      }
      ```
  - **Email Verification**: When a user signs up, they will receive a verification email with a link similar to:
    ```
    https://piyushraivds45.pythonanywhere.com/Authentication/activate/<uidb64>/<token>/
    ```
    The user needs to visit this link to activate their account.

## Running Tests Locally

To run the tests, use the following command:

```sh
python manage.py test
