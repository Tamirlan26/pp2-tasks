import re
text = "hello world hello"
a=re.findall(r"^hello",text)
print(a)