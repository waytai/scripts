#########################################################################
#-*- coding:utf-8 -*-
# File Name: rc.py
#########################################################################
#!/bin/python
#!/bin/python
def crypt(data, key):
    """RC4 algorithm"""
    x = 0
    box = range(256)
    for i in range(256):
        x = (x + box[i] + ord(key[i % len(key)])) % 256
        box[i], box[x] = box[x], box[i]
    x = y = 0
    out = []
    for char in data:
        x = (x + 1) % 256
        y = (y + box[x]) % 256
        box[x], box[y] = box[y], box[x]
        out.append(chr(ord(char) ^ box[(box[x] + box[y]) % 256]))
    return ''.join(out)

data = "input data for test"
key = "testkeyl"

en_data = crypt(data, key)

to_encode_data2 = ''.join(hex(ord(c)) for c in en_data)
print to_encode_data2


de_data = crypt(en_data, key)
print de_data
to_decode_data2 = ''.join(hex(ord(c)) for c in de_data)
print to_decode_data2


