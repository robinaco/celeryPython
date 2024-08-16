FROM python:3.12.4

WORKDIR /app

ADD requirements.txt requirements.txt

RUN set -ex \
    && apt-get update && apt-get upgrade -y \
    && apt-get install -y \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt


ADD . .

# Establecer variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "integration_payment_provider.wsgi.application"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
