#########################################################################
# -*- coding:utf-8 -*- 
# File Name: server.py
# Author: wayne
# mail: @163.com
# Created Time: 2016/5/13 14:39:52
#########################################################################
#!/bin/python
import SimpleHTTPServer
import SocketServer

PORT = 8080

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
