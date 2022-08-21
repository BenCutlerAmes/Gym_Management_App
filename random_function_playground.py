import datetime


d = datetime.date.today()
delta = datetime.timedelta(days=7)

print(d.isoweekday())
next_week = d + delta
print (next_week)