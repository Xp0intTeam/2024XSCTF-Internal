#!/bin/bash
/mysql.sh &
sleep 5s && \
    mysql -e "source /init.sql" && \
    mysql -e "alter user 'root'@'localhost' identified by '123456';"

rm /init.sql
apache2ctl start

echo "start.sh finished"