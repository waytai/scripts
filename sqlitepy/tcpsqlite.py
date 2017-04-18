#########################################################################
#-*- coding:utf-8 -*-
# File Name: tcpsqlite.py
#########################################################################
#!/bin/python
import sqlite3
import uuid
import datetime

deviceid = uuid.uuid1()
createtime = datetime.datetime.now()
lasttime = datetime.datetime.now()
ip = '192.168.0.1'
port = '8100'
lng = '2.0000000'
lat = '2.0000000'
latchswitch = 1
caselost = 1


def insert_sql(deviceid, createtime, lasttime, ip, port, lng, lat, latchswitch, caselost):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    conn.execute("INSERT INTO device_device (deviceid, createtime, lasttime, ip, port, lng, lat, latchswitch, caselost) \
                  VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', %d, %d)"%(deviceid, createtime, \
                  lasttime, ip, port, lng, lat, latchswitch, caselost));
    conn.commit()
    cursor.close()
    conn.close()

insert_sql(deviceid, createtime, lasttime, ip, port, lng, lat, latchswitch, caselost)

