# Django Authentication Project

This project implements a user authentication system using Django. It includes features for user registration, login, and logout.

## Features

- **User Registration:** Users can sign up with a unique username and password.
- **User Login:** Registered users can log in using their credentials.
- **User Logout:** Logged-in users can log out of their accounts.
- **Protected Views:** Certain views are accessible only to authenticated users.

## Project Structure

- `auth/`: Contains the Django application for authentication.
- `templates/user/`: HTML templates for user-related pages.
- `user/`: Contains views and forms related to user authentication.
- `manage.py`: Django's command-line utility for administrative tasks.
- `db.sqlite3`: SQLite database file.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/khaledkamr/django-authentication.git
   cd django-authentication
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply the migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   
   Open your web browser and navigate to `http://127.0.0.1:8000/` .