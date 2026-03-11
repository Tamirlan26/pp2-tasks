import re
text = "cat cot cut c9t ct"
a=re.findall(r"c.t",text)
print(a)