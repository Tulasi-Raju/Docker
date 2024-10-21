FROM python:3.9-slim

WORKDIR /home/data

COPY script.py .
COPY IF.txt .
COPY AlwaysRememberUsThisWay.txt .

RUN mkdir output

CMD ["python", "script.py"]
