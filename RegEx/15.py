import re
text = "a ab abb abbb ac"
a=re.findall(r"ab*",text)
print(a)