Add `basic_app` to INSTALLED_APPS

Run migrations

```
python manage.py migrate
```

Create app migrations

```
python manage.py makemigrations basic_app
```

Run migrations again

```
python manage.py migrate
```

Install bcrypt

```
pip install bcrypt
```

Install argon

```
pip install "argon2-cffi>=16.1.0"
```

Add `PASSWORD_HASHERS` and `TEMPLATES_DIR`, `STATIC_DIR`, `MEDIA_DIR`

-----

Creating UserProfileInfo model

Install pillow

```
pip install pillow
```

When adding models or modifing admin create and run migrations

```
python manage.py makemigrations
python manage.py migrate
```
