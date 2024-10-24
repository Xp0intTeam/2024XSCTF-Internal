# 使用 Python 的基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录的内容到容器内的 /app
COPY . .

# 安装依赖
RUN pip install pycryptodome

# 暴露服务端口
EXPOSE 9999

# 运行 Python 代码
CMD ["python", "guess_number.py"]
