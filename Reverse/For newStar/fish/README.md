- **题目名称：** fish
- **题目类型：** Reverse
- **题目难度：** 简单
- **出题人：** bag
- **考点：**

1. aspack脱壳
2. 简单的aes

- **描述：** 魔法口袋附近有一条跟随小鱼，你知道小鱼去哪了吗？
- **flag：**XSCTF{n0w_y2u_kn@w_Wh3rE_!s_Th4_Fi9h}
- **Writeup：**

aspack工具脱壳。

简单的aes

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
def generate_key(key_list):
    for i in range(len(key_list) - 1, 0, -1):
        key_list[i] ^= key_list[i - 1]
    return bytes(key_list)

def aes_ecb_decrypt(raw_output, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = unpad(cipher.decrypt(raw_output), AES.block_size)
    return decrypted.decode('utf-8')

key = [49, 66, 29, 116, 7, 88, 43, 26, 42, 94, 54, 105, 2, 103, 30, 63]
aes_key = generate_key(key)

result = [0x2b, 0x8a, 0x86, 0xef, 0xab, 0x14, 0x61, 0x3e,
          0x94, 0x0c, 0x86, 0x15, 0x49, 0x09, 0x08, 0xb5,
          0x47, 0x2c, 0xb9, 0xa7, 0xbb, 0xd4, 0x39, 0x86,
          0xaf, 0x82, 0xcb, 0x22, 0x90, 0x51, 0x79, 0x69,
          0x95, 0xf3, 0xaa, 0x0d, 0x0d, 0xbc, 0xbd, 0x2f,
          0x35, 0x7b, 0xa1, 0x45, 0xa9, 0x60, 0xe6, 0xa0]

raw_output = bytes(result)
decrypted_message = aes_ecb_decrypt(raw_output, aes_key)
print("flag:", decrypted_message)
```

