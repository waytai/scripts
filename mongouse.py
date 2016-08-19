#########################################################################
#-*- coding:utf-8 -*-
# File Name: new.py
#########################################################################
#!/bin/python

from base.models.task import Task 
taskid = '569e03f8b1aede5426cdad62'
task=Task.objects.get(id=taskid)
print task.renting_order
task.renting_order.phone = "12345678912"
task.save()
print task.renting_order
