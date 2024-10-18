from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import base64


class User():
    key =base64.b64encode(os.urandom(16))
    def __init__(self) -> None:
        pass
    @classmethod
    def generate_key(cls):
        return cls.key
    def encrypt(self,plain_text, key):
        """使用 AES-CBC 模式加密数据"""
        cipher = AES.new(key, AES.MODE_CBC)
        iv = cipher.iv 
        padded_text = pad(plain_text.encode(), AES.block_size)  
        cipher_text = cipher.encrypt(padded_text) 
        return base64.b64encode(iv + cipher_text).decode() 

    def decrypt(self,cipher_text_b64, key):
        """使用 AES-CBC 模式解密数据"""
        cipher_bytes = base64.b64decode(cipher_text_b64)
        iv = cipher_bytes[:AES.block_size]
        cipher_text = cipher_bytes[AES.block_size:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_text = cipher.decrypt(cipher_text)
        return unpad(padded_text, AES.block_size).decode()