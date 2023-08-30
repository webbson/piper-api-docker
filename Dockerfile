FROM python:bookworm

COPY ./src /app
WORKDIR /app
#RUN python3 -m pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

#ENV PYTHONUNBUFFERED=1

CMD ["python", "-u", "/app/server.py"]
