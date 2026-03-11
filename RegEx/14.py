import re
text = "hello world hi there"
a=re.findall(r"\w+\s\w+",text)
print(a)