FROM ubuntu:22.04
ENV GZCTF_FLAG=flag{not_here}
RUN apt-get update
RUN apt install -y xinetd
RUN useradd  -m ctf

WORKDIR /home/ctf

RUN cp -R /usr/lib* /home/ctf

RUN mkdir /home/ctf/dev && \
    mknod /home/ctf/dev/null c 1 3 && \
    mknod /home/ctf/dev/zero c 1 5 && \
    mknod /home/ctf/dev/random c 1 8 && \
    mknod /home/ctf/dev/urandom c 1 9 && \
    chmod 666 /home/ctf/dev/*
RUN mkdir /home/ctf/bin && \
    cp /bin/sh /home/ctf/bin && \
    cp /bin/ls /home/ctf/bin && \
    cp /bin/cat /home/ctf/bin && \
    cp /lib/x86_64-linux-gnu/libc.so.6 /home/ctf && \
    cp /lib64/ld-linux-x86-64.so.2 /home/ctf

COPY pwn.xinetd /etc/xinetd.d/pwn
RUN sed -i "s/PORT/$PORT/" /etc/xinetd.d/pwn
COPY c_master_plus c_master_plus
RUN chmod +x c_master_plus
RUN chown -R root:ctf /home/ctf && chmod -R 750 /home/ctf
COPY run-xinetd.sh run-xinetd.sh
RUN chmod 774 run-xinetd.sh
CMD ["./run-xinetd.sh"]

EXPOSE 9999
#EXPOSE $PORT
#ENTRYPOINT ["timeout","60","runuser", "guest", "-c", "/home/guest/mario"]
