FROM python:3.13-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . ./

EXPOSE 8000

CMD ["gunicorn", "-c", "python:pyquocca.gunicorn", "-w", "1", "app:app"]