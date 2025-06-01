FROM python:3.9
WORKDIR /app

COPY src/requirements.txt .

RUN pip install -r requirements.txt

COPY . .
CMD ["python", "app/app.py"]
