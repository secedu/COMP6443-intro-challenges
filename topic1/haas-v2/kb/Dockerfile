FROM python:3.13-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . ./

EXPOSE 5000

CMD python3 app.py