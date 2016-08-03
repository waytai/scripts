# -*- coding: utf-8 -*-
from datetime import datetime
last_time = "2016-03-07 07:12:44.797000"

d_last_time = datetime.strptime(last_time, "%Y-%m-%d %H:%M:%S.%f")
print d_last_time


import uuid
us = uuid.uuid1()
print us, type(us)
