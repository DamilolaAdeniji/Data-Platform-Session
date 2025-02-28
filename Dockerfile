FROM python:3.10-slim

WORKDIR /PDE

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .

CMD ["python","main.py"]