from datetime import datetime,timedelta
a=input()
b=input()
c=datetime.strptime(a,"%y.%m.%d")
d=datetime.strptime(b,"%y.%m.%d")
e=(d-c)
print(e.total_seconds()/3600)