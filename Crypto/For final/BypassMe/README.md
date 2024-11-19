* **题目名称：** BypassMe

* **题目类型：** CRYPTO
* **题目难度：** (简单)

* **出题人：** HvAng

* **考点：**  

1. ElGamal签名方案，选择签名伪造
2. 分组模式之OFB

* **描述：**  Are you Bob?

* **flag：** XSCTF{0582d54a-a311-4327-9d05-6f15c091a0db}

* **hint：** ElGamal、有些东西是固定的

* **Writeup：**

首先，要看出来它是一个数字签名方案(题目的注释)，然后搜索对比可以得到是`ElGamal`数字签名方案，只需要看最后的验证过程即可       
这里我们可以选择消息进行签名得到`(r,s)`，同时公钥也是可以拿到的(主要是拿到p)，关键是要使得        
$g^{m}\equiv g^{m'}\equiv y^{r}r^{s}(mod\ p)$       
我们已知`m`，使`m' = m + k*(p-1)`即可，这里是费马小定理的一个应用       
![](https://pic1.zhimg.com/80/v2-adb3f6da452b31564230aea1107cc62c_1440w.png)       
<https://ctf-wiki.org/crypto/signature/elgamal/#_15>       
然后通过验证，拿到`AES_OFB`加密后的图片数据，同时还有加密用的`key`       
`OFB`的工作模式如下       
![](https://picx.zhimg.com/80/v2-8919a56c20e8e383d6df19ad5d60304e_1440w.png)       
我们已知`png`的固定前十六字节，将它与加密后的数据的前十六字节异或即可得到下一分组的`iv`

```py
from pwn import *
from Crypto.Util.number import *
from Crypto.Cipher import AES

p = remote('localhost', 8888)
context(arch='amd64', os='linux', log_level='debug')
p.recvline()
p.recvline()
p.recvline()
pub0 = int(p.recvline().decode())
p.recvline()
p.recvline()
p.recvline()
m = long_to_bytes(bytes_to_long(b'Bob')+pub0-1)
p.send(m)
p.recvline()
p.recvline()
r = int(p.recvline().decode())
p.recvline()
s = int(p.recvline().decode())
p.recvline()
p.recvline()
p.send(str(r).encode())
p.recvline()
p.send(str(s).encode())
p.recvline()
p.recvline()
enc_data = long_to_bytes(int(p.recvline().decode(), 16))
p.recvline()
key = long_to_bytes(int(p.recvline().decode(), 16))
png_head = bytes.fromhex('89504e470d0a1a0a0000000d49484452')
iv = xor(enc_data[:16], png_head)
aes = AES.new(key=key, mode=AES.MODE_OFB, iv=iv)
dec_data = png_head+aes.decrypt(enc_data[16:])
with open("secret.png", 'wb')as f:
    f.write(dec_data)
p.recvline()
p.interactive()
# XSCTF{0582d54a-a311-4327-9d05-6f15c091a0db}
```
