#########################################################################
# File Name: local.sh
# Author: wayne
# mail: @163.com
# Created Time: 2016年07月07日 星期四 11时12分50秒
#########################################################################
#!/bin/bash
HELLO=Hello 
function hello {
        local HELLO=World
        echo $HELLO
}
echo $HELLO
hello
echo $HELLO
