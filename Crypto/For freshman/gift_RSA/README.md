* **题目名称：** gift RSA

* **题目类型：** CRYPTO

* **题目难度：** (简单)

* **出题人：** HvAng

* **考点：**  

1. 欧拉定理验证RSA解密

* **描述：**  出题人给了你一个欧拉大礼包，看你是否真的掌握了RSA的解密

* **flag：** XSCTF{H3re_i5_@_Gif7_f0r_y0u_From_Euler:)))))!}

* **Writeup：**

$e*d=k*\phi(n)+1,根据欧拉定理有,a与n互素,a^{\phi(n)}\equiv 1(mod\ n),m^{e*d}\equiv m(mod\ n)\equiv c^{d}(mod\ n)$

```py
from Crypto.Util.number import *
...
print(long_to_bytes(pow(gift, e, n)).decode())
```
