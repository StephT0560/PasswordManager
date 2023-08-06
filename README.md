# Password Manager
This is a Django project that allows users to store and manage passwords securely. It also provides a password generator to create strong random passwords.

#### Features
* User registration and login
* Secure password storage using bcrypt
* Password generator with options for length, symbols, numbers etc.
* View all stored passwords
* Search passwords
* Copy passwords to clipboard

## Usage
Clone the repo:
```git clone https://github.com/yourname/password-manager.git```

Create and activate a virtual environment:
```
python -m venv env
source env/bin/activate
Install dependencies: 
```
Run migrations:
```
python manage.py migrate
```
Create admin user:
```
python manage.py createsuperuser
```
Run development server:
```
python manage.py runserver
```
The app will be available at http://localhost:8000.

Register a new user account and login. You can now add, view, search and manage your passwords.
