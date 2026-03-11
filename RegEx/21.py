import re
text = "cat cats dog dogs bird"
a=re.findall(r"(cat|dog)s",text)
print(a)