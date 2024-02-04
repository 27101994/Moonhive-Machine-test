# Real Estate Management System

## Requirements

- **Python Version:** 3.8.10
- **Database:** SQLite

## Installation

1. **Install virtualenvwrapper-win:**

   ```bash
   pip3 install virtualenvwrapper-win


2. Create a new virtual environment:

   ```bash
   mkvirtualenv your_project_env
   

3. Activate the virtual environment:

   ```bash
   workon your_project_env
   

4. Install Django inside the virtual environment:

   ```bash
   pip3 install django
   

5. Install project dependencies:

   ```bash
   pip3 install -r requirements.txt
   

## Database Setup

1. **Setup SQLite Database:**

   ```bash
   # Run migrations to create SQLite database tables
   python manage.py migrate
   

2. ## Update Django Settings for SQLite:

2.1. Open the `settings.py` file in your Django project.

2.2. Locate the `DATABASES` configuration in the settings file. It should look something like this:

   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / "real_estate.sqlite3",
       }
   }

## Database Migrations:

To create and apply database migrations:

1. Apply migrations to create the database arrangements:

   ```bash
   python manage.py migrate
   

## Run server

Run the development server:

   ```bash
   python manage.py runserver


