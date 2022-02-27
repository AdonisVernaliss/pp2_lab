import datetime
import random

current_datetime = datetime.datetime.now()
rday = datetime.datetime(random.randint(0, current_datetime.year), random.randint(1, 12), random.randint(1, 30))
tday = datetime.datetime.now()

diff = tday - rday
print(diff.total_seconds())
