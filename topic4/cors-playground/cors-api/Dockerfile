FROM python:3.13-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . ./

EXPOSE 5000

CMD ["gunicorn", "-c", "python:pyquocca.gunicorn", "-b", "0.0.0.0:5000", "app:app"]