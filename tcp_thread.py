#########################################################################
#-*- coding:utf-8 -*-
# File Name: test.py
#########################################################################
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket
import threading
import time

sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#sock.connect(('msp01.claaiot.com',30002))
HOST = 'localhost' 
PORT = 8001

def tcpclient(sock):
    sock.connect((HOST, PORT))
    while True:
        sock.send("send mqtt message for test")
        time.sleep(2)
 
def tcpserver(sock):
    sock.bind((HOST, PORT))
    sock.listen(5)
    
    print 'Server start at: %s:%s' %(HOST, PORT)
    print 'wait for connection...'
    
    while True:
        conn, addr = sock.accept()
        print 'Connected by ', addr
    
        while True:
            data = conn.recv(1024)
            print data
            conn.send("server received you message.")


class TcpClientThread(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.sock = sock

    def run(self):
        tcpclient(self.sock)

class TcpServerThread(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.sock = sock

    def run(self):
        tcpserver(self.sock)

if __name__=='__main__':
    tcpserver_thread  = TcpServerThread(sock_server)
    tcpserver_thread.start()
    tcpclient_thread = TcpClientThread(sock_client)
    tcpclient_thread.start()



