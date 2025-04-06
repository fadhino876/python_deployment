from python:3.11.11-alpine3.21
label description="My first python app deployment"
workdir /app
COPY ./app/ .
run pip install -r requirements.txt
add read.txt read.txt
expose 8081
# cmd ["pytest"]
# cmd ["python", "main.py"]

