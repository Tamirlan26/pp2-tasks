import re
text = "cat dog bird dog cat fish"
a=re.findall(r"cat|dog",text)
print(a)