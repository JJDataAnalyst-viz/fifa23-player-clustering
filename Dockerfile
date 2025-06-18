FROM python:3.13.5-slim-bookworm

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir  -r requirements.txt

COPY . .

RUN adduser --disabled-password --gecos '' appuser

RUN chown -R appuser:appuser /app

USER appuser

ENV FLASK_APP=app.py

EXPOSE 80

CMD ["sh","-c","python -m main && flask run --host=0.0.0.0 --port=80"]
