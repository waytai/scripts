#########################################################################
# File Name: pg.sh
# Author: haha
# mail: @163.com
# Created Time: 2016年08月31日 星期三 16时11分32秒
#########################################################################
#!/bin/bash

#psql --host=host --port=5432 --username=postgres --password --dbname=dbname
#psql --host=host --port=5432 --username=rdsadmin --password 
#psql --host=localhost --port=5432 --username=postgres --password --dbname=iot

#nc -zv host 5432

#pg_restore -h host -p 5432 -U postgres  -d fogcloud_test_20  example.sql

#psql -h host -p 5432 -U postgres -d example -f example.sql

psql --host=host --port=5432 --username=postgres --password 
