# Django Blog Project

A simple blog application built using Django. This project allows users to create, read, and manage blog posts. Users can register, log in, and create new blog entries.

## Features

- User registration and authentication
- Create, read, and delete blog posts
- Organized display of posts
- Simple and clean front-end design

## Technologies Used

- Django
- SQLite (default database)
- HTML/CSS
- Bootstrap (for styling)
- Python

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package manager)
- Django (version specified in `requirements.txt`)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/saurav-tamta-sharma/Django-blog.git
   cd Django-blog

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt

4. **Apply migrations:**

    ```bash
    python manage.py migrate

5. **Run the development server:**

    ```bash
    python manage.py runserver

6. **Access the application:** Open your web browser and go to http://127.0.0.1:8000/.

## Usage

1. **Register a New Account**: Create an account to start posting blogs.
2. **Log In**: Use your credentials to log in to your account.
3. **Create New Blog Posts**: Access the post creation feature from your account dashboard.
4. **View All Posts**: See all published blog posts on the home page.

## Admin Access

To access the Django admin panel, create a superuser account:

    ```bash
    python manage.py createsuperuser

Then log in to the admin panel at http://127.0.0.1:8000/admin/ using the superuser credentials.

