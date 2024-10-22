* **题目名称：**RSA_CBC

* **题目类型：** CRYPTO

* **题目难度：**中等

* **出题人：**Haruka

* **考点：**  

1. RSA加密算法

2. CBC分组加密模式

3. LCG

* **描述：**  Crypto小伙CTF偶遇CBC学长，题题秒杀实力强如全栈，拼劲全力无法战胜。于是它竟然派出RSA和CBC学长融为一体了！快救救CBC学长！

* **flag：**XSCTF{CBC:Nob0dy_kn0ws_R5A_b3tt3r_7han_me!!}

* **Writeup：** 

  ```python
  from Crypto.Util.number import *
  
  c = [10546544657184270108056865326461575390, 2974691170743307765063461696404543720, 7904512473237371909364213640796031312, 8698645797826644152560800118783553896, 1512288316727882848681192590012642566, 12802077922569556544361235996959934847, 3843434733700439914702127192140089064]
  x1 = 6185949729345418624
  x2 = 5408295634577722073
  x3 = 175658213257022173
  x4 = 4142629054947753441
  x5 = 4361315035816873430
  x6 = 5664670762003653105
  
  n = GCD((x6-x5)*(x4-x3)-(x5-x4)**2,(x5-x4)*(x3-x2)-(x4-x3)**2)
  a = (x3-x2)*pow(x2-x1,-1,n)%n
  b = (x2-a*x1)%n
  
  def invLCG(a, b, x, n):
      while 1:
          x = pow(a, -1, n) * (x - b) % n
          yield x
  
  invlcg = invLCG(a, b, x1, n)
  iv = long_to_bytes(next(invlcg))[:7]
  pub_key = []
  while len(pub_key) < 2 + len(c):
      i = next(invlcg)
      if isPrime(i):
          pub_key = [i] + pub_key
  e = pub_key[:-2]
  p = pub_key[-2]
  q = pub_key[-1]
  d = [pow(e_, -1, (p-1)*(q-1)) for e_ in e]
  
  def CBC_decode(c, iv, d, N):
      msg = []
      for i in range(len(c)):
          if i != 0:
              iv = long_to_bytes(c[i-1])[:7]
          mi = pow(c[i], d[i], N)
          msgi = bytes([long_to_bytes(mi)[j] ^ iv[j] for j in range(7)])
          msg.append(msgi)
      return msg
  
  print(b''.join(CBC_decode(c, iv, d, p*q)))
  
  
  ```

  
