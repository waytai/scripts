#########################################################################
# File Name: env.sh
# Author: wayne
# mail: @163.com
# Created Time: 2016年05月08日 星期日 09时27分23秒
#########################################################################
#!/bin/bash

echo "start"
Path="/home/wayne/.virtualenvs/liu"
if [ ! -d  "$Path" ]; then
    echo "make liu"
    mkvirtualenv liu
else
    source `which virtualenvwrapper.sh`
    workon mxchip
fi
