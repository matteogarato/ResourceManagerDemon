#!/bin/sh
sudo git pull
nohup python3.5 ResourceManagerDemon.py > /dev/null 2>&1 &