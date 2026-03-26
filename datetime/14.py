from datetime import datetime
a=input()
b=datetime.strptime(a,"%H:%M:%S")
c=b.hour*3600+b.minute*60+b.second
print(c)