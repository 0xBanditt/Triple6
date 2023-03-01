# checkin ofc  
import sys
if sys.version_info<(3,0):
   sys.stderr.write("\nYou need python 3.0 or later to run this script\n")
   sys.stderr.write("Please update and make sure you use the command python3 geo-recon.py <IP NUMBER> <COMMAND>\n\n")
   sys.exit(0)

# Import magic 
import requests
import json
from colorama import Fore, Back, Style
import os
from plugins.commands import command
from plugins.commands import listCommand
from plugins.nmapVulnScan import nmapVuln 
from plugins.ping import ping
from plugins.help import help
from plugins.getData import getGeo
from plugins.checkip import check
from plugins.nmapVerify import verify 

# color n shit 
R = Fore.RED
B = Fore.BLUE
G = Fore.GREEN
C = Fore.CYAN
Y = Fore.YELLOW
M = Fore.MAGENTA
W = Fore.WHITE
RE = Fore.RESET 

# Background Color
BR = Back.RED
BB = Back.BLUE
BG = Back.GREEN
BC = Back.CYAN
BY = Back.YELLOW
BM = Back.MAGENTA
BW = Back.WHITE
BRE = Back.RESET 

# The thing which does the CLI thingy 
syA = sys.argv

# Logo here 'cuz I'm lazy 
Logo = (f"""
{R}

            ______              
       .d$$$******$$$$c.        
    .d$P"            "$$c      |''||''|                     '||`         ,,,,  
   $$$$$.           .$$$*$.       ||            ''           ||         ||   ' 
 .$$ 4$L*$$.     .$$Pd$  '$b      ||    '||''|  ||  '||''|,  ||  .|''|, ||''|, 
 $F   *$. "$$e.e$$" 4$F   ^$b     ||     ||     ||   ||  ||  ||  ||..|| ||  || 
d$     $$   z$$$e   $$     '$.   .||.   .||.   .||.  ||..|' .||. `|...  `|..|' 
$P     `$L$$P` `"$$d$"      $$                       ||                        
$$     e$$F       4$$b.     $$                      .||                        
$b  .$$" $$      .$$ "4$b.  $$ 
$$e$P"    $b     d$`    "$$c$F 
'$P$$$$$$$$$$$$$$$$$$$$$$$$$$  {C}            {Y}OSINT{C} tool for IP lookup   {RE}{R}
 "$c.      4$.  $$       .$$   {M}           Type --help or -h for help        {RE}{R}
  ^$$.      $$ d$"      d$P    {M}     Type --commands or -c to show commands  {RE}{R}
    "$$c.   `$b$F    .d$P"     
      `4$$$c.$$$..e$$P"        
          `^^^^^^^`
{RE}                        Author   :  0xbanditt
                        GitHub   :  https://github.com/0xBanditt/Triple6
{RE}{BRE}
""") 

# Main stuff 
def welcome():
    print(Logo)

# CLI if no args are passed 
def zero(syA):
    if (len(sys.argv) == 1):
        welcome()
    else:
        verify()
zero(syA)

# CLI management 
if (len(sys.argv) > 1):
    syA1 = sys.argv[1]
    if sys.argv[1].startswith("-"):
        # help 
        if syA1 == "--help" or syA1 == "-h":
            os.system("clear")
            welcome()
            listCommand()

        # kool banner 
        elif syA1 == "-b" or syA1 == "--banner":
            os.system("clear")
            welcome()

    else:
        os.system("clear")
        welcome()
        print(Fore.GREEN + '\n Wait a minute....' + Fore.RESET)
        getGeo(syA1)
        check(syA1)

# if we got parameters more than 2 
if (len(sys.argv) > 2):
    syA1 = sys.argv[1]
    syA2 = sys.argv[2]
    nmapVuln(syA2, syA1)
    command(syA2, syA1)
    ping(syA2, syA1)
    
