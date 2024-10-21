* **题目名称：** Baby_xor

* **题目类型：** CRYPTO

* **题目难度：** (简单)

* **出题人：** HvAng

* **考点：**  

1. 简单的异或算法

* **描述：**  你知道异或吗？

* **flag：** XSCTF{n0t_On1y_th3_st4rt_But_4l50_th3_3nD!!!!!!!}

* **Writeup：**

根据`XSCTF{}`确定异或的秘钥

```py
from Crypto.Util.number import *
cipher = b'672:/\x1a\n^\x10.!\x07P\x1d1\x10\x19]6\x12\x10Z\x16\x051+\x14\x101P\x1d[Y>\x10\x06W.]\x07%EOEPOH@\x19'
key = ''
head = b'XSCTF{}'
for i in range(6):
    key += chr(cipher[i] ^ head[i])
key += chr(cipher[-1] ^ head[-1])
for i in range(len(cipher)):
    print(chr(cipher[i] ^ ord(key[i % 7])), end='')
```