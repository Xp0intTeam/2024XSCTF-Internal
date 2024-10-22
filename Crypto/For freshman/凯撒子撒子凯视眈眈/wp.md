#### 凯撒子撒子凯视眈眈

##### ぬん！

新生专属题，以古典密码为背景，意在让新生对python脚本有一个初步的接触和认知。

```
def s_hi_ka(text):
    offset = 1
    enc = ''
    for w in text:
        if w in string.ascii_letters:
            enc += chr(ord(w) + offset)
        else:
            enc += w
        offset *= -1
    return enc
```

分析代码可知，这是一个变种凯撒加密。偏移量在1与-1之间切换。

**需要注意的是对于非字母字符偏移量照样会变化。**

解一：将原加密函数的offset变量改成-1即得解密脚本，直接扔密文进去就行。

```
import string


def decrypt(text):
    offset = -1
    enc = ''
    for w in text:
        if w in string.ascii_letters:
            enc += chr(ord(w) + offset)
        else:
            enc += w
        offset *= -1
    return enc


enc_flag = "YRDSG{L@J_T@_M0JP_ONLN_MPJ0_L0PNP0_RIH_S@M!_U@O!!!}"
print(decrypt(enc_flag))
```

解二：由于本题的偏移量过于友好，看懂加密的话手搓也可以简单地还原明文。

```
XSCTF{K@I_S@_N0KO_NOKO_NOK0_K0OOO0_SHI_T@N!_T@N!!!}
```

