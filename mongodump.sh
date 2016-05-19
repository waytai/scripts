#########################################################################
# File Name: mongodump.sh
# Author: wayne
# mail: @163.com
# Created Time: 2016年05月19日 星期四 10时45分57秒
#########################################################################
#!/bin/bash

mongodump -h ip:27017 -d mqtt_client -o mqtt_test
