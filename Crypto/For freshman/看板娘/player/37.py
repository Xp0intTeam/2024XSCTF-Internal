from Crypto.Util.number import *
base = 37
flag = b'XSCTF{test_flag}'
m = bytes_to_long(flag)
secret = []
while m:
    secret.append(m % base)
    m //= base
print(f'secret = {secret}')
"""
secret = [7, 31, 11, 36, 32, 34, 27, 8, 10, 7, 5, 35, 0, 0, 1, 4, 27, 30, 28, 16, 7, 12, 10, 24, 13, 15, 17, 1, 12, 13, 18, 23, 6, 26, 36, 0, 21, 36, 23, 21, 32, 13, 25, 5, 15, 21, 20, 1, 7, 36, 3]
"""
