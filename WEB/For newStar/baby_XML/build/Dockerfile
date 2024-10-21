FROM ubuntu:16.04

RUN sed -i 's/http:\/\/archive.ubuntu.com\/ubuntu\//http:\/\/mirrors.tuna.tsinghua.edu.cn\/ubuntu\//g' /etc/apt/sources.list && \
    sed -i '/security/d' /etc/apt/sources.list && \
    apt-get update -y && \
    apt-get install -y curl unzip apache2 php php-mysql php-curl libapache2-mod-php php-cli php-mcrypt php-mbstring php-ldap php-xml php-sqlite3 && \
    a2enmod rewrite && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD entrypoint.sh /
ENTRYPOINT ["bash", "/entrypoint.sh"]
RUN /etc/init.d/apache2 restart && \
    rm /var/www/html/index.html

ADD index.php /var/www/html
ADD people.jpg /var/www/html

RUN useradd -ms /bin/bash  fl4444449g && \
    useradd -ms /bin/bash  1n && \
    useradd -ms /bin/bash  r0ot && \
    useradd -ms /bin/bash  direct0ry && \
    echo "<WFNDVEZ7eTAwMDAwdV9yXzlvMG8wbzBvMG8wZF80dF9YeEV9>" > /fl4444449g
EXPOSE 80
