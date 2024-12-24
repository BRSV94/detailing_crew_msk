FROM --platform=linux/arm64 python:3.9

WORKDIR /app

RUN pip install gunicorn==20.1.0 

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

WORKDIR /app/detailing_crew_msk

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "detailing_crew_msk.wsgi"]
# CMD python manage.py makemigrations && python manage.py migrate && python manage.py add_cars_models && gunicorn detailing_crew_msk.wsgi:application --bind 0.0.0.0:8000
# CMD python manage.py makemigrations && python manage.py migrate && python manage.py add_cars_models && python manage.py runserver
# CMD ["python", "manage.py", "runserver", "0:8000"]
