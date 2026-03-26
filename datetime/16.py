from datetime import datetime
import calendar
a=datetime(2026,3,14,23,25,15)
b=a.replace(hour=23, minute=0, second=0)
print(b)