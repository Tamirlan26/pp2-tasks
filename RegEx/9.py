import re
text = "I love my dog"
a=re.findall(r"dog$",text)
print(a)