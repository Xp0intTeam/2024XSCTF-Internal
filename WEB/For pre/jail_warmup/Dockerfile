FROM python:3.10-slim-bullseye

COPY app.py /app/
COPY flag /flag
RUN python3 -m pip install flask && chmod 777 /flag

CMD ["python3","/app/app.py"]