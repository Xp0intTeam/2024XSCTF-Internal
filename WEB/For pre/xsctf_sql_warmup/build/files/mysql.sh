#!/bin/bash
while :
do
    su mysql -c "mariadbd --datadir=/mysql/data --user=mysql"
done

