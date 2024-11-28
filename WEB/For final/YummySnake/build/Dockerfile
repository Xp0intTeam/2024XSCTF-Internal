FROM python:3.9

RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list && \
    sed -i 's/security.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
RUN apt-get update

WORKDIR /app

COPY ./app /app

RUN python3 -m pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

ENV GZCTF_FLAG=XSCTF{[GUID]}

CMD ["python", "app.py"]

EXPOSE 5000
