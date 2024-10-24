from Crypto.Util.number import *
import socketserver
import socket
import random
import time
import os

flag = os.environ.get('GZCTF_FLAG').encode()

class Task(socketserver.BaseRequestHandler):
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
        a = getPrime(128)
        b = getPrime(128)
        n = getPrime(128)
        x = random.getrandbits(128)
        cnt = 0
        print(n,a,b)
        self.request.settimeout(60)

        for _ in range(9):
            
            x = (a * x + b) % n
            
            if cnt == 4:
                self.send(b"**************************************")
                secret = str(x).encode()
                print(secret)
            else:
                self.send(str(x).encode())
            cnt += 1
            time.sleep(0.3)
        
        self.send(b'What is the **************************************')

        try:
                client_send = self.recv()
        except socket.timeout:
            self.send(b"Connection timed out due to inactivity. Closing connection.")
            exit()

        if client_send == secret:
            self.send(b'\nBingo!!! Flag is '+flag)
        self.send(b"\nConnection has been closed")
        self.request.close()


class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 9999
    server = ThreadedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    print(f"Serving on {HOST}:{PORT}")
    server.serve_forever()
