import re
text = "go goo gooo g"
a=re.findall(r"go+",text)
print(a)