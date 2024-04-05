FROM python:3.12.2-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app/

COPY requirements.txt /app/

EXPOSE 8000

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]