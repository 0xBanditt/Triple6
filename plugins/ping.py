import requests
import sys
import json
import time
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

def ping(syA2, syA1):
    print("#####################################\n")
    if syA2 == "-p" or syA2 == "--ping":
        print(f"{Y}----------{B} Pinging : {R}{syA1}{Y}----------{RE}")
        os.system(f"ping {syA1}")
        exit(0)

    else:
        print('Review the command after the IP, \nwrite python geo-recon.py --command or -c to see the avaliables commands')
        print(" ")
