FROM openjdk:8u322-slim

COPY app /app

WORKDIR /app
RUN useradd ctf\
    && echo "XSCTF{81f989bf-31d2-4f82-93a9-2c2ee44630d8}" > /flag

USER ctf
CMD ["java", "-jar", "/app/Hessian_checkin-1.0-SNAPSHOT.jar"]