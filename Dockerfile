FROM robd003/python3.10 

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "notes.py"]
