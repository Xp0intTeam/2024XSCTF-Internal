#!/usr/bin/env bash
echo $GZCTF_FLAG > /home/ctf/flag && export FLAG=not && FLAG=not
/etc/init.d/xinetd restart
sleep infinity
