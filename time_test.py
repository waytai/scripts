#########################################################################
#-*- coding:utf-8 -*-
# File Name: time_test.py
#########################################################################
#!/bin/python
from datetime import datetime
from datetime import timedelta
t1 = datetime.now()
minute_num = t1.minute
if minute_num >= 30:
    delta = minute_num - 30
else:
    delta = minute_num

t2 = t1 - timedelta(minutes=delta)
print t2

every_delta = 20

dt = datetime.strptime("2016-05-17 16:30:00", "%Y-%m-%d %H:%M:%S")
print dt
