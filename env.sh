#########################################################################
# File Name: env.sh
# Author: wayne
# mail: @163.com
# Created Time: 2016年05月08日 星期日 09时27分23秒
#########################################################################
#!/bin/bash

echo "start"

echo $HOME

if [ ! -d  ".virtualenvs/liu" ]; then
    echo "hello"
    mkvirtualenv liu
fi
workon liu
