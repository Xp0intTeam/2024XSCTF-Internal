#!/bin/sh

rm -f /docker-entrypoint.sh

# Get the user
user=$(ls /home)

# Check the environment variables for the flag and assign to INSERT_FLAG
# 需要注意，以下语句会将FLAG相关传递变量进行覆盖，如果需要，请注意修改相关操作

INSERT_FLAG="XSCTF{I_jUSt_turn3d_18_dont_gu3ss_thAt}"

# 将FLAG写入文件 请根据需要修改
echo $INSERT_FLAG | tee /18.php

chmod 744 /18.php

php-fpm & nginx &

echo "Running..."

tail -F /var/log/nginx/access.log /var/log/nginx/error.log