#!/bin/bash

mysql -uroot < /db.sql

# 修改数据库中的 FLAG
mysql -e "USE student;CREATE TABLE \`2333\` (\`id\` int NOT NULL,\`name\` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,\`class\` int NOT NULL,\`whatcanisay\` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,PRIMARY KEY (\`id\`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;INSERT INTO \`2333\` VALUES ('114514', '小美爱$FLAG', '3', '到此一游，我终于考到梦中情校了哈哈哈，想知道在哪里吗，去partC找吧哈哈哈');" -uroot

export FLAG=not_flag
FLAG=not_flag

exec supervisord -n



