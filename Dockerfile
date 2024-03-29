FROM python:3.9.6-slim

WORKDIR /app
COPY ./ ./
RUN pip install -r requirements.txt
ENV PYTHONPATH=/app
ENTRYPOINT python ./service.py