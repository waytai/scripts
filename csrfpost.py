#########################################################################
#-*- coding:utf-8 -*-
# File Name: iotpost.py
#########################################################################
#!/bin/python
import json
import requests
http_url = "test_url"

client = requests.session()
client.get(http_url)
csrftoken = client.cookies['csrftoken']
data = {"identification": "name","password":'123456', 'csrfmiddlewaretoken':csrftoken, 'next':'/'}

dict_headers = {
        "Referer":http_url,
        #"X-CSRFToken":csrftoken
        "Cookie":"csrftoken=%s"%csrftoken
        }
r = requests.post(http_url, data=data, headers=dict_headers)
tt = r.text
print tt

