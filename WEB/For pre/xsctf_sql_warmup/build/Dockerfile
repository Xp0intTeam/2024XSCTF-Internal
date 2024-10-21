FROM ubuntu:22.04


# change apt source
RUN sed -i 's/http:\/\/archive.ubuntu.com/http:\/\/mirrors.aliyun.com/g' /etc/apt/sources.list && \
sed -i 's/http:\/\/security.ubuntu.com/http:\/\/mirrors.aliyun.com/g' /etc/apt/sources.list && \
echo nameserver 223.5.5.5 > /etc/resolv.conf

# avoid block when configuring tzdata
ENV DEBIAN_FRONTEND=noninteractive
# install mariadb php apache
RUN apt update && \
apt install php php-mysql mariadb-server-core-10.6 mariadb-client-core-10.6 -y


# copy source file and set priv

#copy file 1
RUN mkdir /app
COPY files/ /app/files

RUN rm /var/www/html/* && \
    #setup web file
    cp /app/files/index.php /var/www/html/ && \
    chown root:root -R /var/www && \
    chmod 755 -R /var/www && \

    #setup db
    mkdir -p /run/mysqld /mysql/data /mysql/base /mysql/plugin && \
    useradd mysql && \
    chown mysql:mysql -R /run/mysqld /mysql && \
    su mysql -c "mysql_install_db --datadir=/mysql/data" && \

    cp /app/files/start.sh /start.sh && \
    cp /app/files/init.sql /init.sql && \
    cp /app/files/mysql.sh /mysql.sh && \
    chmod 700 /start.sh /mysql.sh && \
    chmod 600 /init.sql && \
    rm -rf /app

WORKDIR /
CMD /start.sh && sleep infinity