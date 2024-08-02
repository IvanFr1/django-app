FROM python:3.11

ENV PYTHONUNBUFFERED=1


WORKDIR /app

RUN pip install --upgrade pip "poetry==1.8.3"

RUN poetry config virtualenvs.create false --local
COPY pyproject.toml poetry.lock ./
RUN poetry install


COPY . /app

# CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]
# CMD ["python", "mysite/manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000", "--chdir", "/app/mysite"]
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "mysite.wsgi:application"]
