FROM python:3.13-alpine

RUN apk add gcc musl-dev

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . ./

WORKDIR /
RUN head -c 15 /dev/urandom | base64 -w 0 > /password.txt && chmod 400 /password.txt
RUN cat /password.txt | md5sum | cut -d' ' -f1 > /.password.txt.md5

COPY util/getpassword.c /getpassword.c
RUN gcc getpassword.c -o getpassword && chmod +s getpassword && rm getpassword.c

WORKDIR /app
EXPOSE 8000

RUN adduser -s /bin/sh -H app -D
USER app

CMD ["gunicorn", "-c", "python:pyquocca.gunicorn", "app:app"]