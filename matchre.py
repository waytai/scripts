#########################################################################
#-*- coding:utf-8 -*-
# File Name: test2.py
#########################################################################
#!/bin/python
import re
raw_data = "6803294804E26043D25BF43DF372D141FFFFFFFF04E26043BC7CEC3D9591CC416D7217461ACA793FF2167C3F6B16"
raw_data2 = "6803294804E26043D25BF43DF372D141FFFFFFFF04E26043BC7CEC3D9591CC416D7217461ACA793FF2167C3F6B1"
pattern = re.compile(r'^68.+16$')
match = pattern.match(raw_data)
if match:
    print raw_data

match2 = pattern.match(raw_data2)
if match2:
    print raw_data2

