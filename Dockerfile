FROM python:3.12-alpine

WORKDIR /usr/app

COPY requirements.txt /usr/app

RUN pip install --no-cache-dir -r /usr/app/requirements.txt

COPY . /usr/app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]