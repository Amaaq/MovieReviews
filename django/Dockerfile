FROM python:3.12.2-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app/

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000
