#!/usr/bin/env python
import socket
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost',8001))
time.sleep(2)
while True:
    sock.send("data sss")
    time.sleep(2)
    print sock.recv(1024)
sock.close()
