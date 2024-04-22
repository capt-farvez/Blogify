# Blogify - A Django Blogging Platform

Blogify is a web application built using Django that allows users to create, edit, and manage blog posts. It also provides user authentication features.

## Features

- User registration and login
- Account editing (profile picture, bio, etc.)
- Password reset and forgot password functionality
- Create, update, and delete blog posts
- View other users' blog posts

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/capt-farvez/blogify.git
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   # On Windows: venv\Scripts\activate # On Linux: source venv/bin/activate

   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

6. Access the application at http://localhost:8000/


## License

This project is licensed under the MIT License - see the LICENSE file for details.
