from datetime import datetime,timedelta

today = datetime.now()
yesterday=today+timedelta(days=2)
x=yesterday-today
print(x.strftime("%M"))