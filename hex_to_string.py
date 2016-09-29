#########################################################################
#-*- coding:utf-8 -*-
# File Name: test.py
#########################################################################
#!/bin/python
a = "hello".encode('hex')
b = "hello"
new_key = ''.join(str(hex(ord(c))) for c in b)
print a ,type(a)
print new_key
print a.decode('hex')
n = new_key.replace('0x','')
print n.decode('hex')
