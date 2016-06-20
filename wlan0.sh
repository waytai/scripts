#########################################################################
# File Name: wlan0.sh
# Author: wayne
# mail: @163.com
# Created Time: 2016年06月20日 星期一 11时24分52秒
#########################################################################
#!/bin/bash
tcpdump -i wlan0 host 115.239.210.27
tcpdump -i wlan0 src host 115.239.210.27
tcpdump -i wlan0 dst host 115.239.210.27
