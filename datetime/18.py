import re
test = 'match.group(1).replace(" ", "").replace(",", ".")'
a=re.match(r"[A-Za-z]+\.[A-Za-z]+",test)
if a:
    print(a.group())
else:
    print("none")


