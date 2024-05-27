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
