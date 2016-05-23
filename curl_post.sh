#########################################################################
# File Name: curl_post.sh
# Author: wayne
# mail: @163.com
# Created Time: 2016年05月23日 星期一 14时36分42秒
#########################################################################
#!/bin/bash

#curl -d http://127.0.0.1:8000/snippets/
#the post request using curl
curl -d "code=print '123'" http://127.0.0.1:8000/snippets/
