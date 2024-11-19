from Crypto.Util.number import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import random
import os
import socketserver


# I think you will definitely be interested in the content in PNG!


class BypassMe(socketserver.BaseRequestHandler):
    def _recvall(self):
        BUFF_SIZE = 2048
        data = b''
        while True:
            part = self.request.recv(BUFF_SIZE)
            data += part
            if len(part) < BUFF_SIZE:
                break
        return data.strip()

    def send(self, msg, newline=True):
        try:
            if newline:
                msg += b'\n'
            self.request.sendall(msg)
        except:
            pass

    def recv(self):
        return self._recvall()

    def handle(self):
        # get_pngdata
        with open("secret.png", "rb") as f:
            png_data = pad(f.read(), 16)

        # get_Key
        bits = 1024
        p = getPrime(bits)
        g = getPrime(bits // 2)
        d = random.randint(1, p - 2)
        y = pow(g, d, p)
        pub, pri = (p, g, y), d

        self.send(
            b"[+] Hello! I'm Alice. To ensure that you are truly Bob, I need to verify your identity first!")
        self.send(
            b"[+] Can I help you sign once? Is there anything you need to sign?")
        self.send(b"[+] Here are your public key:")
        self.send(str(pub[0]).encode())
        self.send(str(pub[1]).encode())
        self.send(str(pub[2]).encode())

        self.send(b"[+] Give me what you need to sign:")
        message = self.recv()

        # Signature
        if message == b"Bob":
            self.send(b"[+] No, it's not possible!!!")
            exit()
        else:
            self.send(b"[+] Here are your sign:")
            while True:
                k = random.randint(1, p - 1)
                if GCD(k, p - 1) == 1:
                    break
            r = pow(g, k, p)
            s = ((bytes_to_long(message) - d * r)
                 * inverse(k, p - 1)) % (p - 1)
            self.send(b"[+] r =")
            self.send(str(r).encode())
            self.send(b"[+] s =")
            self.send(str(s).encode())

            # Verity
            self.send(
                b"[+] Tell me your signature so that I know you are truly Bob.")
            self.send(b"[+] r = ")
            r = int(self.recv().decode())
            self.send(b"[+] s = ")
            s = int(self.recv().decode())

            if pow(g, bytes_to_long(b'Bob'), p) == (pow(y, r, p) * pow(r, s, p)) % p:
                self.send(
                    b"[+] I have a great photo that I would like to share with you. Let's send it to you in our old way! Hope you still keep our IV!")
                key = os.urandom(16)
                aes = AES.new(key, AES.MODE_OFB, iv=os.urandom(16))
                enc_data = aes.encrypt(png_data).hex()
                self.send(b"[+] Here is my encoded data:")
                self.send(str(enc_data).encode())
                self.send(b"[+] Here is my key:")
                self.send(str(hex(bytes_to_long(key))[2:]).encode())
                self.send(b"[+] In summary, I wish you a wonderful day!")
                self.request.close()
            else:
                self.send(
                    b"[+] Alright, you're not Bob, I don't have anything to chat with anymore.")
                self.request.close()


class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 8888
    server = ThreadedServer((HOST, PORT), BypassMe)
    server.allow_reuse_address = True
    print(f"Serving on {HOST}:{PORT}")
    server.serve_forever()
