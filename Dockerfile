FROM python:3.11

ENV PYTHONUNBUFFERED=1


WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

# CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]
# CMD ["python", "mysite/manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000", "--chdir", "/app/mysite"]
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "mysite.wsgi:application"]
