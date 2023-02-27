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
      print(f"{R}Review the IP or type {W}'python Triple3.py -c' for more info.{RE}")

def listCommand():
      print(f'       {BG}{R}# Commands{RE}{BRE}\n')
      print(f'{B}$ {R}python Triple6.py --help or -h                   {BB}{R}(Display help){BRE}')
      print(f'{B}$ {R}python Triple6.py 138.121.128.19 --nmap or -n    {BB}{R}(Nmap standard use [normal scan]){BRE}')
      print(f'{B}$ {R}python Triple6.py 138.121.128.19                 {BB}{R}(Standard use, infos about IP.){BRE}')
      print(f'{B}$ {R}python Triple6.py --commands or -c               {BB}{R}(Display commands available.){BRE}') 
      print(f'{B}$ {R}python Triple6.py 123.456.789.10 --ping or -p       {BB}{R}(Ping a website or an IP){BRE}')
      print(f'{B}$ {R}python Triple6.py 123.456.789.10 --nmap-vuln or -nV {BB}{R}(Uses custom nmap scripts to scan for vulnerabilities on a network)')
      print(RE)

