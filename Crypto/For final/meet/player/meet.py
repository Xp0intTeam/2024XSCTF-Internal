from hashlib import sha256
from random import choices
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from secret import flag


def Key_Gen(chars, length):
    key = []
    for _ in range(6):
        key.append(sha256(bytes(choices(chars, k=length))).digest())
    return key


def encrypt(msg, key):
    p = b'Have_@_Good_Fun!'
    for i in range(6):
        p = AES.new(key[i], AES.MODE_ECB).encrypt(p)
    enc_key = sha256(b"".join(key)).digest()
    enc_flag = AES.new(enc_key, AES.MODE_ECB).encrypt(pad(msg, AES.block_size))
    return p, enc_flag


chars = b'xsAES'
key = Key_Gen(chars, 3)
cipher = encrypt(flag, key)
print(f'c = {cipher[0].hex()}')
print(f'enc_flag = {cipher[1].hex()}')
"""
c = 3f9b376d07e5f6633ed23ca74a502fbe
enc_flag = 641ec79497a475265aa424fe9d8df460ddd495991e92084a65063f0b08a04159547214a81038661557ee9da8685bc7e7e45f73936e3c3f2fad09181f2e33cf45
"""
