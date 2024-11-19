FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install pycryptodome

EXPOSE 8888

CMD ["python", "task.py"]