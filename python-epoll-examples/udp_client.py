#########################################################################
#-*- coding:utf-8 -*-
# File Name: udp_client.py
#########################################################################
#!/bin/python
import socket
BUFSIZE = 1024

#address = ('127.0.0.1', 9999)
#address = ('123.56.184.37', 16802)
#address = ('123.56.184.37', 16802)
#address = ('dtdev.elaas.io', 16802)
address = ('localhost', 8888)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = raw_input()
    if not msg:
        break
    s.sendto(msg, address)
    data,ADDR = s.recvfrom(BUFSIZE)
    print "-"*10, data, ADDR
s.close()
