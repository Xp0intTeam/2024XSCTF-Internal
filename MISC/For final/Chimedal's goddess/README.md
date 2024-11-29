* **题目名称：** Chimedal's goddess

* **题目类型：** MISC

* **题目难度：** (中等)

* **出题人：** HvAng

* **考点：**  

1. base62编码
2. CCIR476 transmission

* **描述：**  Chimedal带上了99朵玫瑰，决定给心心念念的女神表白了，可女神却给他一张小纸条，上面是一段奇奇怪怪的信息，如果Chimedal能破解这段信息的话，女神就答应跟他在一起。作为Chimedal最好的朋友的你，能否帮Chimedal抱得美人归呢？      
解出来的信息请包裹上XSCTF{}

* **flag：** XSCTF{S1LLY IT M4K3S 5ENS3 T0 GO TW0_W4Y}

* **Writeup：**

第一步，附件名字base62解码得到`CCIR476 transmission`，然后开搜    
<https://en.wikipedia.org/wiki/CCIR_476>       
<https://blog.gcwizard.net/manual/en/ccitt-codes/08-what-is-ccir-476/>      
<https://github.com/AI5GW/CCIR476>       
`CCIR476`传输编码是一种用于无线电数据通信的编码方式，它使用两个不同的字符表：一个用于字母，一个用于数字和符号。这种编码方式通过控制字符在字母模式和数字/符号模式之间切换。下面是它的编码表，控制字符是`0x5a/0x36`       
![](https://blog.gcwizard.net/wp-content/uploads/2022/02/ccir476-2.png)

```py
from Crypto.Util.number import *
bin_list = '101101010010110110110010111010110101100101110010101010111101010100110111101001101010011100101101101010101101101000111100110110101011010110101001011110101001101101110100101101010101101011001100101101101101010110110101010110101110100011011001011011101010101101001101011110001110101011101000100111011011001011011000111101101001001110110110101010110110100101011'
letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
          'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '\r', '\n', 'li', 'fi', ' ', ' ']
figure = ['_', '?', ':', '$', '3', '!', '&', '#', '8', '\'',
          '(', ')', '.', ',', '9', '0', '1', '4', '*', '5', '7', ';', '2', '/', '6', '"', '\r', '\n', 'li', 'fi', ' ', ' ']
table = [0x47, 0x72, 0x1d, 0x53, 0x56, 0x1b, 0x35, 0x69, 0x4d, 0x17, 0x1e, 0x65,
         0x39, 0x59, 0x71, 0x2d, 0x2e, 0x55, 0x4b, 0x74, 0x4e, 0x3c, 0x27, 0x3a, 0x2b, 0x63, 0x78, 0x6c, 0x5a, 0x36, 0x5c, 0x6a]
dict1 = dict(zip(table, letter))
dict2 = dict(zip(table, figure))
mode = 0
flag = ''
for i in range(0, len(bin_list), 7):
    b = int(bin_list[i:i+7], 2)
    if b == 0x5a:   # Letters mode
        mode = 1
        continue
    elif b == 0x36: # Figures mode
        mode = 0
        continue
    if mode == 1:
        flag += dict1[b]
    elif mode == 0:
        flag += dict2[b]
print("XSCTF{"+flag+"}")
```
