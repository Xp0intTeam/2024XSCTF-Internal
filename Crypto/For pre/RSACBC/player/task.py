from Crypto.Util.number import *
import random
from secret import flag

assert len(flag) == 44

while 1:
    a, b, x, n = [random.randint(1, 1<<64) for i in 'CBC_yyds!'][:4]
    if isPrime(n):
        break

def LCG(a, b, x, n):
    while 1:
        x = (a * x + b) % n
        yield x

def padding(msg):
    block_num = (len(msg) // 7) + 1
    return msg.ljust(block_num * 7, b'\0')

def CBC(msg, iv, e, N):
    block_num = len(msg) // 7
    c = []
    for i in range(block_num):
        msgi = [msg[i*7+j] ^ iv[j] for j in range(7)]
        mi = bytes_to_long(bytes(msgi))
        ci = pow(mi, e[i], N)
        c.append(ci)
        iv = long_to_bytes(ci)[:7]
    return c

lcg = LCG(a, b, x, n)
pub_key = []
while len(pub_key) <= 2 + (len(flag) // 7):
    i = next(lcg)
    if isPrime(i):
        pub_key.append(i)
e = pub_key[:-2]
N = pub_key[-2] * pub_key[-1]
iv = long_to_bytes(next(lcg))[:7]
c = CBC(padding(flag), iv, e, N)
print(c)
for i in 'CBC_orzorzorz'[-6:]:
    print(next(lcg))

'''
[10546544657184270108056865326461575390, 2974691170743307765063461696404543720, 7904512473237371909364213640796031312, 8698645797826644152560800118783553896, 1512288316727882848681192590012642566, 12802077922569556544361235996959934847, 3843434733700439914702127192140089064]
6185949729345418624
5408295634577722073
175658213257022173
4142629054947753441
4361315035816873430
5664670762003653105
'''
