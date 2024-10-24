* **题目名称：** guessnumber

* **题目类型：** CRYPTO

* **题目难度：** (简单)

* **出题人：** Stardust

* **考点：**  

1. 流密码LCG

* **描述：**  你能猜出中间的数字吗?

* **flag：**动态flag

* **Writeup：**

```
xs = [...,
      ...,
      ...,
      ...,
      0,
      ...,
      ...,
      ...,
      ...]

ts = [xs[i+1] - xs[i] for i in range(len(xs)-1)]
m = gcd((ts[0]*ts[2]-ts[1]^2),ts[5]*ts[7]-ts[6]^2)
a = (xs[2]-xs[1])*inverse_mod(xs[1]-xs[0],m) % m
b = (xs[1]-a*xs[0]) % m
xs[4] = (xs[3]*a+b) % m
print(xs[4])
```

