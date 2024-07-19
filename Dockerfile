FROM python:3.12-slim
WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r /app/requirements.txt --no-cache-dir
COPY . .

CMD ["gunicorn", "weather_app.wsgi:application", "--bind", "0:8000" ]