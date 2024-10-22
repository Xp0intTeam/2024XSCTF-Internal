FROM python:3.6.7

RUN mkdir -p /backend
WORKDIR /backend
COPY src/requirements.txt /backend
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /backend
COPY ./service/docker-entrypoint.sh /

# 指定容器入口点
ENTRYPOINT ["/bin/bash","/docker-entrypoint.sh"]