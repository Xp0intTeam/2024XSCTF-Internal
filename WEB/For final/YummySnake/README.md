* 题目名称： YummySnake

* 题目类型： WEB

* 题目难度： 中等

* 出题人： itSssm3

* 考点：python格式化字符串漏洞

* 描述：
    来玩玩贪吃蛇吧😋

    ⚠TIPS⚠  flag在环境变量里哦 但是要怎么才能看到环境变量呢

* flag： XSCTF{[GUID]}

* Writeup：

    首先先玩一会快乐的贪吃蛇到18分，然后就会发现到了胜利的路由

    发现有一个可以填胜利宣言的页面，想到是python，尝试来尝试去
    
    应该就会通过debug报错看见部分关键源码，分析源码可知存在格式化字符串漏洞

    可以利用的方式有很多，这里举一个例子

    看上面的`emojis.`的各种调用，`emojis`是一个对象，并且有`__init__`方法

    使用exp：

    ```
    {emojis.__init__.__globals__[app].__init__.__globals__[os].environ}
    {emojis.__init__.__globals__[app].wsgi_app.__globals__[os].environ}
    ```
    
    即可读到flag


