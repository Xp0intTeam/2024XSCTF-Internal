* **题目名称：** Meet

* **题目类型：** CRYPTO
* **题目难度：** (中等)

* **出题人：** HvAng

* **考点：**  

1. 中间相遇攻击

* **描述：**  你说，我们还能再见面吗？

* **flag：** XSCTF{M17m_@t74ck_4nd_VvVvvvVeee3rry_5l0ww_Py7h0n}

* **Writeup：**

中间相遇攻击，两面逼近，以空间换取时间
<https://ctf-wiki.org/crypto/attack-summary/meet-in-the-middle/>
$c=E_{k6}(E_{k5}(E_{k4}(E_{k3}(E_{k2}(E_{k1}(p))))))$
$p=D_{k1}(D_{k2}(D_{k3}(D_{k4}(D_{k5}(D_{k6}(c))))))$
$E_{k3}(E_{k2}(E_{k1}(p)))=D_{k4}(D_{k5}(D_{k6}(c)))$
原来遍历所有的可能是$(5^{3})^{6}=3814697265625$种，现在是$(5^{3})^{3}*2=3906250$种，`exp`大概跑一分多就可以出了

```py
from Crypto.Util.number import *
from hashlib import sha256
from Crypto.Cipher import AES
import itertools
from time import *

start = time()
c = 0x3f9b376d07e5f6633ed23ca74a502fbe
enc_flag = 0x641ec79497a475265aa424fe9d8df460ddd495991e92084a65063f0b08a04159547214a81038661557ee9da8685bc7e7e45f73936e3c3f2fad09181f2e33cf45
c = long_to_bytes(c)
enc_flag = long_to_bytes(enc_flag)
p = b'Have_@_Good_Fun!'
chars = 'xsAES'
key = []
combinations = list(itertools.product(chars, repeat=3))
list = []
for combo in combinations:
    list.append(''.join(combo).encode())
length = len(list)**3
E_k3_k2_k1_p = []
for k1 in list:
    for k2 in list:
        for k3 in list:
            key1 = sha256(k1).digest()
            key2 = sha256(k2).digest()
            key3 = sha256(k3).digest()
            E_k3_k2_k1_p.append(AES.new(key3, AES.MODE_ECB).encrypt(AES.new(key2, AES.MODE_ECB).encrypt(
                AES.new(key1, AES.MODE_ECB).encrypt(p))))
            key.append(key1+key2+key3)
print('[+] E_k3_k2_k1_p finished')
set1 = set(E_k3_k2_k1_p)
D_k4_k5_k6_c = []
for k4 in list:
    for k5 in list:
        for k6 in list:
            key4 = sha256(k4).digest()
            key5 = sha256(k5).digest()
            key6 = sha256(k6).digest()
            D_k4_k5_k6_c.append(AES.new(key4, AES.MODE_ECB).decrypt(AES.new(key5, AES.MODE_ECB).decrypt(
                AES.new(key6, AES.MODE_ECB).decrypt(c))))
            key.append(key4+key5+key6)
set2 = set(D_k4_k5_k6_c)
res = set1 & set2
print('[+] D_k4_k5_k6_c finished')
res = res.pop()
print(f'[+] res = {res}')
enc_key = []
enc_key.append(key[E_k3_k2_k1_p.index(res)])
enc_key.append(key[length+D_k4_k5_k6_c.index(res)])
enc_key = sha256(b"".join(enc_key)).digest()
print(AES.new(enc_key, AES.MODE_ECB).decrypt(enc_flag))
end = time()
print(f'[+] time = {end-start}')
```