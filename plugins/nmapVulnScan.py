import os
import sys
import colorama
from colorama import Fore, Back, Style

# magic colors 
R = Fore.RED
B = Fore.BLUE
G = Fore.GREEN
C = Fore.CYAN
Y = Fore.YELLOW
M = Fore.MAGENTA
W = Fore.WHITE
RE = Fore.RESET 

def nmapVuln(syA2, syA1):
    # check if nmap custom scripts exists or not... 
    try:
        open("/data/data/com.termux/files/usr/share/nmap/scripts/nmap-vulners/vulners.nse")
    except FileNotFoundError:
        os.system("cd /data/data/com.termux/files/usr/share/nmap/scripts/ && git clone https://github.com/vulnersCom/nmap-vulners.git > /dev/null 2>&1")

    print("##################################### \n")
    if syA2 == "-v" or syA2 == "--vuln":
        print('---------   ----------')
        print(f"{B}It may takes a while.{RE}")
        print('---------------------- \n \n')
        ip = syA1
        nmapadv = os.system("nmap -sV --script vuln " + ip)
        print(nmapadv)
        sys.exit(0)
        
    else:
        print(f"{R}Review the IP or type {W}'python Triple3.py -c' for more info.{RE}")

