
FROM tiangolo/uwsgi-nginx:python3.8-alpine-2020-12-19

COPY . /app
WORKDIR /app

ENV LISTEN_PORT=5000
EXPOSE 5000

RUN pip install --no-cache-dir -r requirements.txt


