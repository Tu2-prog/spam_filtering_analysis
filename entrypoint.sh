if [[ $APP_ENV == "dev" ]]; then
    python manage.py runserver 0.0.0.0:8080
else
    # do something more production-y
    echo "try gunicorn!"
fi
