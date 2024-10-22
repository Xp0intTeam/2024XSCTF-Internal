from Crypto.Util.number import getPrime
from secret import flag

assert len(flag) == 32

nLen = 16
k = [getPrime(256) for i in range(nLen)]

class LFSR:
    # 爆裂黎明：立刻在攻击范围内召唤2个魂灵之影；LLL攻击力+180%，攻击时攻击力提升至220%。
    def __init__(self, seed):
        self.seed = []
        for i in range(nLen):
            self.seed.append(seed & 255)
            seed >>= 8
    def feedback(self):
        self.status = self.seed[0]
        new = 0
        for ki, si in zip(k, self.seed):
            new += ki * si
        self.seed = self.seed[1:] + [new]
        return self.status

flag1 = flag[:nLen]
flag2 = flag[nLen:]
# 立刻在攻击范围内召唤2个魂灵之影
lfsr1 = LFSR(int.from_bytes(flag1,'little'))
lfsr2 = LFSR(int.from_bytes(flag2,'little'))
for i in range(nLen):
    lfsr1.feedback()
    lfsr2.feedback()
out1 = [lfsr1.feedback() for i in range(2*nLen)]
out2 = (lfsr2.feedback() >> 8) << 8
with open('output.txt', 'w') as f:
    f.write('out1 = ' + str(out1) + '\n')
    f.write('out2 = ' + str(out2) + '\n')
