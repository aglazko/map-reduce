import sys
from datetime import datetime
from calendar import day_name

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        dates = data[0]
        sale = data[4]
        weekday1 = datetime.strptime(dates, "%Y-%m-%d").weekday()
        weekdays = list(day_name)[weekday1]
        print("{0}-{1}".format(weekdays, sale))
