FROM openjdk:8u222-slim

ENV flag=XSCTF{Th3n_y0u_can_le4rn_m0re_ab0ut_j4v4_s3curity}

COPY app /app
#COPY --chmod=500 init.sh /init.sh

WORKDIR /app
#RUN adduser -disabled-password -shell /bin/bash www-data
RUN useradd ctf

USER ctf

CMD ["java","-jar","/app/app.jar"]
