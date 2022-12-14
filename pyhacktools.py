import os
import time
import sys
from sys import platform
from tools.BurpSuite  import *
from tools.owaspzap import *
from tools.metasploit import *
from tools.johntheripper import *
from tools.hydra import *
from tools.nmap import *
from tools.zenmap import *
from tools.masscan import *
from tools.tcpdump import *
from tools.wireshark import *
from tools.sqlmap import *
from tools.aircrackng import *
from tools.wpscan import *
from tools.nikto import *
from tools.Wapiti import *


clear = lambda: os.system('clear')

black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"

error  = f"{blue}[{white}!{blue}] {red}"

success = f"{yellow}[{white}√{yellow}] {green}"

ask  =     f"{green}[{white}?{green}] {yellow}"

info  =   f"{yellow}[{white}+{yellow}] {cyan}"

info2  =   f"{green}[{white}•{green}] {purple}"

clear()

def check_os():

      os = platform

      
      if os == 'win'.lower() and 'win32'.lower():
            time.sleep(0.5)
            print(f'\n{error}Этот скрипт только для линукса(Debian Ubuntu)\n')
            sys.exit()

      elif os == 'darwin'.lower():
            time.sleep(0.5)
            print(f'\n{error}Этот скрипт только для линукса(Debian Ubuntu)\n')
            sys.exit()

check_os()

menu = f'''{nc}______________________________________________________________________________{nc}

             ____        _   _            _         _              _ 
            |  _ \ _   _| | | | __ _  ___| | __    | |_ ___   ___ | |
            | |_) | | | | |_| |/ _` |/ __| |/ /____| __/ _ \ / _ \| |
            |  __/| |_| |  _  | (_| | (__|   <_____| || (_) | (_) | |
            |_|    \__, |_| |_|\__,_|\___|_|\_\     \__\___/ \___/|_|
                   |___/

                        {info}{yellow}VERSION-TOOL: 1.0{yellow}
                  {info}{yellow}By MYTHON-DEV or MYTH-DEV{yellow}
            {info}{yellow}Instagram: @mython_dev and @hackingworld_d {yellow}               
{nc}______________________________________________________________________________{nc}

\\\ Топ-15 инструментов для пентеста на Linux

{white}1){white} {cyan}Burp Suite{cyan}
{white}2){white} {cyan}OWASP ZAP{cyan}
{white}3){white} {cyan}Metasploit{cyan}
{white}4){white} {cyan}John the Ripper{cyan}
{white}5){white} {cyan}Hydra{cyan}
{white}6){white} {cyan}Nmap{cyan}
{white}7){white} {cyan}Zenmap{cyan}
{white}8){white} {cyan}Masscan{cyan}
{white}9){white} {cyan}tcpdump{cyan}
{white}10){white} {cyan}Wireshark{cyan}
{white}11){white} {cyan}SQLmap{cyan}
{white}12){white} {cyan}AirCrack{cyan}
{white}13){white} {cyan}WPScan{cyan} 
{white}14){white} {cyan}Nikto{cyan}
{white}15){white} {cyan}Wapiti{cyan}

{error}0 Выйти!

'''
print(menu)

def main():
      try:
            choose_tool = input(f'{nc}PyHackTool~# ')
      except KeyboardInterrupt:
            print(f'\n{success}Выход!')
            sys.exit()

      if choose_tool == '1':
            time.sleep(0.5)
            print(description_tool_burpsuite)
            os.system(install_burpsuite)
            print(zapusk_burpsuite)
            
            main()
 
      elif choose_tool == '2':
            time.sleep(0.5)
            print(description_tool_owasp)
            os.system(install_owasp)
            print(zapusk_owasp)

            main()

      elif choose_tool == '3':
            time.sleep(0.5)
            print(description_tool_msf)
            os.system(install_burpsuite)

            print(zapusk_burpsuite)

            main()

      elif choose_tool == '4':
            time.sleep(0.5)
            print(description_tool_john)
            os.system(install_johntheripper)
            print(zapusk_johntheripper)

            main()

      elif choose_tool == '5':
            time.sleep(0.5)
            print(description_tool_hydra)
            os.system(install_hydra)
            print(zapusk_hydra)

            main()
      
      elif choose_tool == '6':
            time.sleep(0.5)
            print(description_tool_nmap)
            os.system(install_nmap)
            print(start_nmap)
            main()
      
      elif choose_tool == '7':
            time.sleep(0.5)
            print(description_tool_zenmap)
            os.system(install_zenmap)
            print(start_zenmap)

            main()
      
      elif choose_tool == '8':
            time.sleep(0.5)
            print(descirption_tool_masscan)
            os.system(install_masscan)
            print(start_masscan)

            main()

      elif choose_tool == '9':
            time.sleep(0.5)
            print(description_tool_tcpdump)
            os.system(install_tcp_dump)
            print(start_tcpdump)

            main()

      elif choose_tool == '10':
            time.sleep(0.5)
            print(description_tool_wireshark)
            os.system(install_wireshark)
            print(start_wireshark)

            main()

      elif choose_tool == '11':
            time.sleep(0.5)
            print(description_tool_sqlmap)
            os.system(install_sqlmap)
            print(start_sqlmap)

            main()

      elif choose_tool == '12':
            time.sleep(0.5)
            print(description_tool_aircrackng)
            os.system(install_aircrackng)
            print(start_aircrackng)

            main()

      elif choose_tool == '13':
            time.sleep(0.5)
            print(description_tool_wpscan)
            os.system(install_wpscan)
            print(start_wpscan)

            main()
  
      elif choose_tool == '14':
            time.sleep(0.5)
            print(description_tool_nikto)
            os.system(install_nikto)
            print(start_nikto)

            main()

      elif choose_tool == '15':
            time.sleep(0.5)
            print(description_tool_wapiti)
            os.system(install_wapiti)
            print(start_wapiti)

            main()
      
   
      else: 
            print(f'\n{error}Нет такого инструмента\n{nc}')
            main()

main()