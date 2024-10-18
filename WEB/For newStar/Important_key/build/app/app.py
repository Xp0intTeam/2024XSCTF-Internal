from flask import Flask,request,json
import pickle
import base64
from verify import *

app=Flask(__name__)

user=User()

def merge(src, dst):
    for k, v in src.items():
        if hasattr(dst, '__getitem__'):
            if dst.get(k) and type(v) == dict:
                merge(v, dst.get(k))
            else:
                dst[k] = v
        elif hasattr(dst, k) and type(v) == dict:
            merge(v, getattr(dst, k))
        else:
            setattr(dst, k, v)

@app.route('/',methods=['POST', 'GET'])
def index():
    if request.method=="GET":
        return "welcome to 2024 XSCTF!"
    elif request.method=="POST":
        try:
            if request.data:
                merge(json.loads(request.data), user)
            return "ok"
        except:
            return "error"

@app.route('/login',methods=['POST'])
def login():
    role=request.form.get("role")
    if role:
        try:
            key=base64.b64decode(User.generate_key())
            if user.decrypt(role,key)=="admin":
                data=request.form.get("data")
                if data:
                    data=base64.b64decode(data)
                    pickle.loads(data)
                    return "ok"
                else:
                    return "Please give me the serialized data!"
        except:
            return "error"
    else:
        return "Please tell me your role!"


if __name__=="__main__":
    app.run(host="0.0.0.0")