FROM python:3.11-slim

ENV PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple

ADD app /app

COPY flaAag.txt /flaAag.txt

WORKDIR /app

RUN pip3 install -r requirements.txt
RUN useradd ctf
USER ctf

CMD ["python3","app.py"]
