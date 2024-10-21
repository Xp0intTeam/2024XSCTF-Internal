FROM tutum/lamp

ENV LANG="C.UTF-8"
COPY ./files/html /app
COPY ./files/mysql-setup.sh mysql-setup.sh
COPY ./db.sql /db.sql
RUN chown -R www-data:www-data /app
#RUN sed -i 's/skip-network/#skip-network/' /etc/my.cnf.d/mariadb-server.cnf
