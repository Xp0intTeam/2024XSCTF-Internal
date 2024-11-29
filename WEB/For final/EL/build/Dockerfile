FROM openjdk:8u222-slim

COPY app /app
#COPY --chmod=500 init.sh /init.sh

WORKDIR /app
#RUN adduser -disabled-password -shell /bin/bash www-data
RUN useradd ctf\
  && echo "XSCTF{Expr3ssi0n_L4ngu4g3_is_v3ry_u5efu1}" > /flag

USER ctf

CMD ["java","-jar","/app/app.jar"]
