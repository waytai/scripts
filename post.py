#########################################################################
#-*- coding:utf-8 -*-
# File Name: post.py
#########################################################################
#!/bin/python
import urllib, httplib
httpClient = None
end_time = '2016-05-17 16:30:00'
try:
    params = urllib.urlencode({'mac_id':'c8-93-e0-02-8c', 'end_time': end_time})
    headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
    httpClient = httplib.HTTPConnection('localhost', 8000, timeout=10)
    httpClient.request('POST', '/wifidevice/user_time_location/', params, headers)
    response = httpClient.getresponse()
    print response.status
    print response.reason
    print response.read()
    print response.getheaders()

except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()
