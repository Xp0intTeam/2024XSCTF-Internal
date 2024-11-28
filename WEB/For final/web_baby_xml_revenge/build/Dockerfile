FROM ubuntu:16.04

RUN sed -i 's/http:\/\/archive.ubuntu.com\/ubuntu\//http:\/\/mirrors.tuna.tsinghua.edu.cn\/ubuntu\//g' /etc/apt/sources.list && \
    sed -i '/security/d' /etc/apt/sources.list && \
    apt-get update -y && \
    apt-get install -y curl unzip apache2 php php-mysql php-curl libapache2-mod-php php-cli php-mcrypt php-mbstring php-ldap php-xml php-sqlite3 && \
    a2enmod rewrite

ADD entrypoint.sh /
ENTRYPOINT ["bash", "/entrypoint.sh"]
RUN /etc/init.d/apache2 restart && \
    rm /var/www/html/index.html

ADD index.php /var/www/html
ADD seCr3t.php /var/www/html
ADD people.jpg /var/www/html

RUN echo "<WFNDVEZ7bjBib2R5X0tuMHdfWHhlX2IzdHRlcl90aDRuX01lfQ==>" > /FLAGflag114514
EXPOSE 80