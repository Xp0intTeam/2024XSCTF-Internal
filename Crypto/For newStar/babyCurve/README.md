* **题目名称：** ezRSA

* **题目类型：** CRYPTO

* **题目难度：** (困难)

* **出题人：** Stardust

* **考点：**  

1. 椭圆曲线上的离散对数 ECDLP
1. 椭圆曲线变换

* **描述：**  

* **flag：**XSCTF{20518cc67b7def9197daa00b8d4ae8335e8f5844fb9e04a4ae94cc62a7aa4636}

* **Writeup：**

本体难点在于椭圆曲线的变换与映射.

从题给的加法乘法能看出原曲线是Hessian曲线, 这里有该曲线的全部数据https://www.hyperelliptic.org/EFD/g1p/data/hessian/coordinates

按照这里的数据写出映射函数, 最后的离散对数用sage的函数一把梭即可

```py
#sage
from Crypto.Util.number import *
from gmpy2 import *
from hashlib import sha256

def coefficients(d):
    '''
    a4 = -27 d(d^3+8)
    a6 = 54(d^6-20 d^3-8)
    '''
    a4 = -27 * d * (pow(d, 3, p) + 8) % p
    a6 = 54 * (pow(d, 6, p) - 20 * pow(d, 3, p) - 8) % p
    return [a4,a6]

def toweierstrass(d,x,y):
    '''
    toweierstrass u = 12(d^3-1)/(d+x+y)-9 d^2
    toweierstrass v = 36(y-x)(d^3-1)/(d+x+y)
    '''
    u = (12 * (pow(d, 3, p) - 1) * inverse_mod(d+x+y,p) - 9 * pow(d, 2, p)) % p
    v = 36 * (y - x) * (pow(d, 3, p) - 1) * inverse_mod(d+x+y,p) % p
    return u,v

def fromweierstrass(d,u,v):
    '''
    fromweierstrass x = (36(d^3-1)-v)/(6(u+9 d^2))-d/2
    fromweierstrass y = (v+36(d^3-1))/(6(u+9 d^2))-d/2
    '''
    t1 = 36 * (pow(d, 3, p) - 1) % p
    t2 = 6 * (u + 9*pow(d, 2, p)) % p
    x = ((t1 - v) * pow(t2, -1, p) % p) - d*inverse_mod(2, p) % p
    y = ((v + t1) * pow(t2, -1, p) % p) -d*inverse_mod(2, p) % p
    return x,y

p = 14774086086310024849
d = 10346898339886066613
G = (12636797399455969005, 4656307018278399363)
P = (6616434244263216394, 6830441955370423062)

a4,a6 = coefficients(d)
E = EllipticCurve(Zmod(p),[a4,a6])
G_ = E(toweierstrass(d,G[0],G[1]))
P_ = E(toweierstrass(d,P[0],P[1]))
k = P_.log(G_)
# k = G_.discrete_log(P_) 低版本用这个
# k = 124652458607932645
flag = 'XSCTF{' + sha256(str(k).encode()).hexdigest() + '}'
print(flag)
```