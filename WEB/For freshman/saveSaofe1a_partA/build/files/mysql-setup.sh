#!/bin/bash

mysql -uroot < /db.sql

# 修改数据库中的 FLAG
mysql -e "USE student;INSERT INTO \`class3\` VALUES ('114514', '小美', '3', '做ctf题目并找到flag:$FLAG');" -uroot

export FLAG=not_flag
FLAG=not_flag

exec supervisord -n



