FROM dangerfarms/geodrf-alpine:latest
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
ADD requirements.dev.txt /app/
RUN pip install -r requirements.dev.txt -U
RUN pip install -t .lib -r requirements.dev.txt -U
ADD . /app/
