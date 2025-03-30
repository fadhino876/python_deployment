from python:3.11.11-alpine3.21
label description="My first python app deployment"
volume /app
workdir /app
COPY ./* /app/
env CALL_MY_NAME="Tegar"
run pip install -r requirements.txt
add read.txt /app/
expose 8081
cmd ["python", "main.py"]

