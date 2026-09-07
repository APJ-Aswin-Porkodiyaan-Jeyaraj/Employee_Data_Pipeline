from python:latest

WORKDIR /app

copy requirements.txt
run pip install -r requirements.txt

copy . .

cmd["python", "main.py"]