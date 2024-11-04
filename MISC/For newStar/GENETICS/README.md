* **题目名称：** GENETICS

* **题目类型：** MISC

* **题目难度：** (中等)

* **出题人：** HvAng

* **考点：**  

1. DNA编码

* **描述：**  Bing，Bing，Bing！DNA的碱基也可以用来编码啦！

* **flag：** XSCTF{y0u_r3@lly_kn0w_th3_secr3t_be7ween_g3net1cs_@nd_b1n4ry}

* **Writeup：**

8种符合互补规则，我们使用的是`AGCT`，而不是第一种比较常规的`ACGT`，所以可能需要遍历8种规则才能得到`flag`
![](https://pic1.zhimg.com/80/v2-2a7bf8b897ab026614d466d7eec59c3c_1440w.png?source=d16d100b)

```py
from Crypto.Util.number import *

dec = [
    {"A": "00", "C": "01", "G": "10", "T": "11", ' ': ''},
    {"A": "01", "C": "00", "G": "11", "T": "10", ' ': ''},
    {"A": "10", "C": "11", "G": "00", "T": "01", ' ': ''},
    {"A": "11", "C": "01", "G": "10", "T": "00", ' ': ''},
    {"A": "10", "C": "00", "G": "11", "T": "01", ' ': ''},
    {"A": "00", "C": "10", "G": "01", "T": "11", ' ': ''},
    {"A": "11", "C": "10", "G": "01", "T": "00", ' ': ''},
    {"A": "01", "C": "11", "G": "00", "T": "10", ' ': ''}
]
# AGCT
s = 'GGCA GGAT GAAT GGGA GAGC GTCT GTCG ATAA GTGG GGTT GTAC ATAT GAAA GCTA GCTA GTCG GGTT GCCT GCTC ATAA GTGT GGTT GTGA GCCA ATAT GGTT GTAT GCGG GCAT GTAC ATAT GTGA GGTT GCAC GCGG ATGT GTGT GCGG GCGG GCTC GGTT GCGT ATAT GCTC GCGG GTGA ATAG GCAT GTAT GGTT GAAA GCTC GCGA GGTT GCAC ATAG GCTC ATGA GTAC GTCG GTTG'
for dict in dec:
    flag = ''
    for i in s:
        flag += dict[i]
    print(long_to_bytes(int(flag, 2)))
```