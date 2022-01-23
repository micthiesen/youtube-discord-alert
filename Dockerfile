FROM python:3.10
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

COPY src /app/src
ENTRYPOINT [ "python", "/app/src/main.py" ]
