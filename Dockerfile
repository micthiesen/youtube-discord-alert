FROM python:3.10-slim
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

COPY src /app/src
EXPOSE 5777:5777
ENTRYPOINT [ "python", "/app/src/main.py" ]
