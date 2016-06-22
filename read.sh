#########################################################################
# File Name: rm.sh
# Author: wayne
# mail: @163.com
# Created Time: 2016年06月22日 星期三 10时25分03秒
#########################################################################
#!/bin/bash

read_dir () {
    for i in $1/*
    do
        if [ -d $i ]
        then
            read_dir $i
        else
            echo $i
        fi
    done

}

read_dir $1
