* **题目名称：**艾伦走路人

* **题目类型：** MISC

* **题目难度：**容易

* **出题人：**Haruka

* **考点：**  

1. 对比替换字符

2. 二进制数转字符串


* **描述：**  

  你在哪?🤔
  亚特兰蒂斯😨
  在海下面🤓👆
  在海下面🤓👆
  你在哪?🤔
  有一个梦😰
  怪兽正在我身体里狂野奔跑😭
  我褪色了😩
  我褪色了😩
  好失落😔
  我褪色了😩
  我褪色了😩
  好失落😔
  我褪色了😵

* **flag：**XSCTF{Y0u_W3r3_7he_5h4d0w_t0_my_1ifE-AlanWalker}

* **Writeup：** 

  ```python
  from Crypto.Util.number import *
  with open('cipher.txt') as f:
      c = f.read().split('\n')
  b = ''
  for i in range(1, len(c)):
      for j in range(len(c[0])):
          if c[0][j] == c[i][j]:
              b += '0'
          else:
              b += '1'
  print(long_to_bytes(int(b,2)))
  ```

  
