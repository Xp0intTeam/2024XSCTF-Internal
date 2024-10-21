* **题目名称：** 恶魔的语言

* **题目类型：** MISC

* **题目难度：** (简单)

* **出题人：** HvAng

* **考点：**  

1. 温州话
2. 十六进制

* **描述：**  All of his emails are in Chinese. Mayfair, we got to get everyone who speaks Chinese. I want all eyes on those emails. Our translators are struggling with it. Apparently it's a very rare dialect, called Wenzhou. The Chinese call it the Devil's language.

* **flag：** XSCTF{nOw_y0u_kn0w_w3nzhou_di4lect}

* **Writeup：**

```py
with open("devil's word.txt", 'r') as f:
    data = f.read().strip().split(' ')
table = {'leng': '0', 'lia': '2', 'sa': '3', 'sii': '4', 'ng': '5', 'leu': '6', 'cai': '7',
         'bo': '8', 'jau': '9', 'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f'}
result = b''
for i in range(0, len(data), 2):
    result += bytes([int(table[data[i]]+table[data[i + 1]], 16)])
print(result.decode())
```