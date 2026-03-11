import re
text = "cat dog cat bird"
a=re.findall(r"cat",text)
print(a)