# Dockerfile
   FROM ubuntu:latest
   RUN apt-get update && apt-get install -y vim python3.10 python3.10-venv python3-pip git
   COPY . .
   RUN pip install --no-cache-dir -r requirements.txt

