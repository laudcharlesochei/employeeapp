# PRT Employee Management System (Django)

This is a Django conversion of the provided Spring Boot + Thymeleaf CRUD app.

## 1) Run locally (SQLite)

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open: http://127.0.0.1:8000/index

## 2) Switch to MySQL locally (optional)

Set `DATABASE_URL` in an environment variable (or create a `.env` file in the project root):

```bash
DATABASE_URL=mysql://USER:PASSWORD@HOST:3306/DBNAME
```

Then run:

```bash
python manage.py migrate
python manage.py runserver
```

## 3) Deploy to Heroku (MySQL)

This project is pre-configured for Heroku:
- `Procfile` uses gunicorn.
- `settings.py` reads `DATABASE_URL` (or `CLEARDB_DATABASE_URL`) from environment variables.
- Static files are served with WhiteNoise.

Typical steps (example):

```bash
heroku create
# Add a MySQL add-on (e.g., ClearDB) or provide DATABASE_URL yourself
git push heroku main
heroku run python manage.py migrate
```

If your MySQL add-on provides `CLEARDB_DATABASE_URL`, the app will use it automatically.
