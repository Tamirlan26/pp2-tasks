import re
text = "a aa aaa aaaa aaaaa aaaaaa"
a=re.findall(r"a{2,4}",text)
print(a)