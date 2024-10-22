* **题目名称：**LLLLfsr!

* **题目类型：** CRYPTO

* **题目难度：**困难

* **出题人：**Haruka

* **考点：**  

1. LLL算法
2. LFSR

* **描述：**  绫香学姐玩维什戴尔玩到目光呆滞了，看到题目上这么多L烦死人，她不耐烦地准备要启动爆裂黎明了！快去阻止她！

* **flag：**XSCTF{e4zy_l3arn1ng_LFSR_&_LLL!}

* **Writeup：** 

  ```python
  flag = b''
  with open('output.txt') as f:
      exec(f.read())
  M1 = Matrix(ZZ,[out1[i:i+16] for i in range(16)])
  b = Matrix(ZZ,[out1[16:]])
  k = b * M1.inverse()
  k = k[0]
  M2 = Matrix(ZZ,[[1 if i == j else 0 for j in range(16)] + [k[i]] for i in range(16)] + [[0 for i in range(16)] + [-out1[0]]])
  flag += bytes(M2.LLL()[0])[:-1]
  M3 = Matrix(ZZ,[[1 if i == j else 0 for j in range(16)] + [k[i]] for i in range(16)] + [[0 for i in range(16)] + [-out2]])
  flag += bytes(M3.LLL()[0])[:-1]
  print(flag)
  ```

  
