#########################################################################
# File Name: backup.sh
# Author: wayne
# mail: @163.com
# Created Time: 2016年07月07日 星期四 11时04分34秒
#########################################################################
#!/bin/bash
OF=my-backup-$(date +%Y%m%d).tgz
tar -czf $OF find.js
echo $(date)
