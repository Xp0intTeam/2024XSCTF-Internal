* **题目名称：** QR

* **题目类型：** CRYPTO

* **题目难度：** (中等)

* **出题人：** HvAng

* **考点：**  

1. 二次剩余

* **描述：**  你知道什么是QR吗？

* **flag：** XSCTF{0h!_y0u_r3ally_knOw_Wh4t_1s_QR_@nd_HoW_7o_c4lcu1a7ing_l3genDre_5ymbOl}

* **Writeup：**

二次剩余，计算勒让德符号

```py
from Crypto.Util.number import *
import sympy as sp
p = 
enc = 
flag = ''
for i in range(len(enc)):
    b = sp.legendre_symbol(enc[i], p)
    if b == 1:
        flag += '0'
    else:
        flag += '1'
print(long_to_bytes(int(flag, 2)).decode())
```
