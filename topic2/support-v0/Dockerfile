FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY ./app /app

EXPOSE 8000

RUN addgroup -g 1337 -S appgroup && adduser -u 1337 -S appuser -G appgroup
USER 1337:1337

VOLUME [ "/tmp" ]

CMD ["gunicorn", "-c", "python:pyquocca.gunicorn", "app:app"]