from datetime import datetime
c=input()
v=datetime.strptime(c,"%d.%m.%Y")
b=v.strftime("%b")
print(b)