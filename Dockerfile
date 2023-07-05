FROM python:3.11.4-alpine
RUN apk update
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY server.py /app/server.py
CMD ["python", "/app/server.py"]
