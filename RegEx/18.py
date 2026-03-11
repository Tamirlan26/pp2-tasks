import re
text = "123 45 6789"
a=re.findall(r"\d{3}",text)
print(a)