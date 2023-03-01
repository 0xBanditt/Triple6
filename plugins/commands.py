import requests
import sys
import json
from colorama import Fore, Back, Style
import os
R = Fore.RED 
B = Fore.BLUE
G = Fore.GREEN
C = Fore.CYAN
Y = Fore.YELLOW
M = Fore.MAGENTA
W = Fore.WHITE
RE = Fore.RESET
BB = Back.BLUE
BG = Back.GREEN 
BRE = Back.RESET

def command(syA2, syA1):
   if syA2 == '--nmap' or syA2 == '-n':
      print('---------   ----------')
      print(f"{B}It may takes a while.{RE}")
      print('---------------------- \n \n')
      ip = syA1
      nmapcc = os.system('nmap ' + ip)
      print(nmapcc)
      sys.exit(0)

   else:
      print(f"{R}Review the IP or type {W}'python Triple3.py -h' for more info.{RE}")

def listCommand():
      print(f'{BG}{R}# Commands{RE}{BRE}\n')
      print(f"{R}optional arguments:{RE}")
      print("""
-h, --help       show this help message and exi
-c, --commamds   shows command dialog
""")
      print(f"{R}options:{RE}")
      print("""
-n, --nmap       Nmap standard use
-p, --ping       Pings the IP
-nV, --nmap-vuln Uses custom nmap scripts to find vulnerabilities on the system's IP 
        """)
      print(f"""{R}Example:{RE}

python3 Triple6.py --help or -h                         (Display this)
python3 Triple6.py 123.456.789.10 --nmap or -n          (Nmap standard use)
python3 Triple6.py 123.456.789.10                       (Standard use, info about IP)
python3 Triple6.py 123.456.789.10 --ping or -p          (Ping a website or an IP)
python3 Triple6.py 123.456.789.10 --nmap-vuln or -nV    (Uses custom nmap scripts to scan for vulnerabilities on a network)
""")
