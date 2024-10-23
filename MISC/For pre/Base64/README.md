* **题目名称：** Base64?!

* **题目类型：** MISC

* **题目难度：** (简单)

* **出题人：** HvAng

* **考点：**  

1. Base64编码隐写

* **描述：**  这真的是Base64吗？

* **flag：** XSCTF{y0u_knOw_hOw_B@se64_work5}

* **Writeup：**

Base64编码对应的标准字母表为A-Za-z0-9+/=，共64字符加一个填充字符=。我们知道一个ASCII字符对应8比特的二进制字符串，2的6次方等于64，所以Base64编码用6位01字符串即可表示，如果加密的ASCII字符数量为3的倍数，那么末尾将不会填充=，因为三个ASCII字符正好可以用四个Base64编码表示，但如果ASCII字符数量模3余1，那么前6位01字符串用Base64编码表示后，还剩2个01字符串，此时填充四个0，用Base64编码表示，再填充两个=；如果ASCII字符数量模3余2，前12个01字符串用Base64编码表示后，还剩4个01字符串，此时填充两个0，用Base64编码表示，再填充一个=。       
以上就是Base64编码的原理，那么如何实现隐写呢？如果我们此时不用0进行填充，而把明文的二进制序列进行依次填充，即可把明文隐写到Base64编码中     
exp如下     
```py
import base64
table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
file = open("base64.txt")
flag = ''
tmpbin = ''

for line in file.readlines():  # 按照行来读取文本
    line = line.strip('\n')
    if (line[-1] == '='):  # 当第一位是‘=’时
        if (line[-2] == '='):  # 当第二位是‘=’时
            i = table.index(line[-3])  # 返回倒数第三位的字符在字典中的位置
            b = bin(i)[2:]  # 二进制化后去掉ob前缀
            b = b.zfill(6)  # 将二进制数填充为6位
            tmpbin += b[-4:]
        else:
            i = table.index(line[-2])  # 返回倒数第二位的字符
            b = bin(i)[2:]
            b = b.zfill(6)
            tmpbin += b[-2:]

length = len(tmpbin) / 8  # 计算数据组数
for i in range(int(length)):
    flag += chr(int(tmpbin[i * 8:i * 8 + 8], 2))  # 对二进制数base64编码处理
print(flag)
```