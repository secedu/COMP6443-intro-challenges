FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

USER nobody
VOLUME [ "/tmp" ]

CMD ["gunicorn", "-c", "python:pyquocca.gunicorn", "app:app"]