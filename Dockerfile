FROM python:3.9

WORKDIR /app

RUN pip install gunicorn==20.1.0 

COPY ../requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "foodgram.wsgi"]
CMD python manage.py makemigrations && python manage.py migrate && python manage.py add_cars_models && gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000
