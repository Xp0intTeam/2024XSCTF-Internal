from Crypto.Util.number import *
from random import *

flag = b'XSCTF{a_test_flag}'
p = getPrime(512)
a = 1999
flag = bin(bytes_to_long(flag))[2:]
enc = []
for bit in flag:
    enc.append(pow(a, (randint(2, p) * randrange(2, p, 2)) + int(bit), p))
with open('output.txt', 'w')as out:
    out.write('p = ' + str(p) + '\n')
    out.write('enc = ' + str(enc))
