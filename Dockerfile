FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y ca-certificates

COPY requirements.txt .
COPY getOrders.py .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "getOrders.py"]
