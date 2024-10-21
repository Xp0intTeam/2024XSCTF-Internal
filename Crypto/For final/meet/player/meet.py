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
