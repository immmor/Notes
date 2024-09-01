FROM python:3.12-slim-bookworm

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "notes.py"]
