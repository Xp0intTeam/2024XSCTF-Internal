* **题目名称：** 看板娘

* **题目类型：** CRYPTO

* **题目难度：** (简单)

* **出题人：** HvAng

* **考点：**  

1. 进制转换

* **描述：**  原来你也……

* **flag：** XSCTF{G3niu5_Sw0rdsm@n_March_7th}

* **Writeup：**

简单的进制转换，base可以为任意进制，这里是37进制

```py
from Crypto.Util.number import *
secret = [7, 31, 11, 36, 32, 34, 27, 8, 10, 7, 5, 35, 0, 0, 1, 4, 27, 30, 28, 16, 7, 12, 10, 24, 13,
          15, 17, 1, 12, 13, 18, 23, 6, 26, 36, 0, 21, 36, 23, 21, 32, 13, 25, 5, 15, 21, 20, 1, 7, 36, 3]
base = 37
flag = 0
for i in reversed(secret):
    flag = flag*base+i
print(long_to_bytes(flag).decode())
```
