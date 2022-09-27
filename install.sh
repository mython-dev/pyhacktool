#!/bin/bash

if [ "$(id -u)" != "0" ]; then
   echo "Этот скрипт должен быть запущен как root"
   exit 1
fi

clear

BLACK='\e[30m'
RED='\e[31m'
GREEN='\e[92m'
YELLOW='\e[33m'
ORANGE='\e[93m'
BLUE='\e[34m'
PURPLE='\e[35m'
CYAN='\e[36m'
WHITE='\e[37m'
NC='\e[0m'
purpal='\033[35m'

echo '''

-------------------------------------------------------------------------
                 ____        _   _                      ® 
                |  _ \ _   _| \ | |_ __ ___   __ _ _ __  
                | |_) | | | |  \| | '_ ` _ \ / _` | '_ \ 
                |  __/| |_| | |\  | | | | | | (_| | |_) |
                |_|    \__, |_| \_|_| |_| |_|\__,_| .__/ 
                       |___/  

                            VERSION-TOOL: 1.0
                        By MYTHON-DEV or MYTH-DEV
                Instagram: @mython_dev and @hackingworld_d
-------------------------------------------------------------------------                
'''

echo $"[✔] Установка ... "

sudo apt update -y && apt upgrade -y
sudo apt install python3 &&  sudo apt install python3-pip 
clear
echo $"[✔] Гатова!... "
sudo python3 pyhacktools.py
