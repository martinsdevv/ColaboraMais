FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY apps/backend/app ./app
COPY infra ./infra

RUN mkdir -p /data

EXPOSE 8000

ENV DB_PATH=/data/colaboramais.db

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]