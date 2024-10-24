from Crypto.Util.number import *
from random import randint
from hashlib import sha256

def add_Hcurve(P, Q):
    if P == (0, 0):
        return Q
    if Q == (0, 0):
        return P
    x1, y1 = P
    x2, y2 = Q
    x3 = (y1 ** 2 * x2 - y2 ** 2 * x1) * inverse(x2 * y2 - x1 * y1, p) % p
    y3 = (x1 ** 2 * y2 - x2 ** 2 * y1) * inverse(x2 * y2 - x1 * y1, p) % p
    return x3, y3

def dou_Hcurve(P):
    x1, y1 = P
    x3 = (y1 * (1 - x1 **3)) * inverse(x1 ** 3 - y1 ** 3, p) % p
    y3 = (x1 * (y1 **3 - 1)) * inverse(x1 ** 3 - y1 ** 3, p) % p
    return x3, y3
    
def mul_Hcurve(n, P):
    R = (0, 0)
    while n > 0:
        if n % 2 == 1:
            R = add_Hcurve(R, P)
        P = dou_Hcurve(P)
        n = n // 2
    return R

p = 14774086086310024849
d = 10346898339886066613
G = (12636797399455969005, 4656307018278399363)
k = randint(0,p)
P = mul_Hcurve(k,G)
flag = 'XSCTF{' + sha256(str(k).encode()).hexdigest() + '}'

# (6616434244263216394, 6830441955370423062)