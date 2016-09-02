#########################################################################
# File Name: wlan.sh
# Author: wayne
# mail: @163.com
# Created Time: 2016年09月02日 星期五 13时41分20秒
#########################################################################
#!/bin/bash

rfkill list

rfkill unblock all
rfkill block all
ifconfig wlan0 up
