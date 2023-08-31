FROM python:slim-bookworm

COPY ./src /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "-u", "/app/server.py"]
