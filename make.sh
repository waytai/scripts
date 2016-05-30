#########################################################################
# File Name: make.sh
# Author: wayne
# mail: @163.com
# Created Time: 2016年05月30日 星期一 18时09分59秒
#########################################################################
#!/bin/bash
gcc -c -fPIC libtest.c
gcc -shared libtest.o -o libtest.so
