#!/usr/bin/env python
import socket
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost',8888))
time.sleep(2)
while True:
    msg = raw_input()
    if not msg:
        break
    sock.send(msg)
    #time.sleep(2)
    print sock.recv(1024)
sock.close()
