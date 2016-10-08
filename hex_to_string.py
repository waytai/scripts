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


test = 'abc'
str_to_hex =''.join(hex(ord(s)) for s in test)
print str_to_hex 

#hex_to_str = str_to_hex.split('0x')
#print hex_to_str
#for element in hex_to_str:
#    if len(element):
#        print chr(int(element,16))

hex_to_str = ''.join(chr(int(element,16))for element in str_to_hex.split('0x') if len(element))
print hex_to_str

