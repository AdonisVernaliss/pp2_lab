import datetime

x = datetime.datetime.now()
one_day = datetime.timedelta(days=1)

yesterday = x - one_day
tomorrow = x + one_day

print(yesterday,"\t",x,"\t",tomorrow)
