import datetime


x = datetime.datetime.now()
five_days = datetime.timedelta(days=5)

x = x - five_days

print(x)
