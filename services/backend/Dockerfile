FROM python:3.10

RUN mkdir app
WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY src/ .
COPY .env .