import re
t="colour cotr color coloer"
a=re.findall(r"colou?r",t)
print(a)