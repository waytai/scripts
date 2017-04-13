#########################################################################
#-*- coding:utf-8 -*-
# File Name: test.py
#########################################################################
#!/bin/python
import base64
def decode_base64(data):
    """Decode base64, padding being optional.
    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.
    """
    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += b'='* missing_padding
    return base64.decodestring(data)

payload_encode = "BgAAAAEAAQ"
payload_decode = decode_base64(payload_encode) 
print payload_decode
payload_encode = payload_encode.strip('\0')
print payload_decode, type(payload_decode)
with open('log.txt', 'a') as f:
    f.write(payload_decode)

if payload_decode == '\x06\x00\x00\x00\x01\x00\x01':
    print "iiii"
