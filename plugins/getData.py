import requests
import sys
import json
from colorama import Fore, Back, Style
import os

# colour n' shit for font
R = Fore.RED
B = Fore.BLUE
G = Fore.GREEN
C = Fore.CYAN
Y = Fore.YELLOW
M = Fore.MAGENTA
W = Fore.WHITE 
RE = Fore.RESET

def getGeo(syA1):
    r = requests.get('http://ip-api.com/json/'+syA1)
    response = json.loads(r.text)

    #Iterate the data, filter & print ( data for specific fields
    print (f"[{B}*{RE}] Running Geo-location Check Against {R}{sys.argv[1]}{RE}") 
    print ("Country: "+ response["country"])
    print ("Region: " + response["regionName"])
    print ("City: " + response["city"])
    print ("Organization: "+response["org"])
    print ("Longitude: ", response["lon"])
    print ("Latitude: ", response["lat"])
    print ("ISP: "+ response["isp"] + "\n") 
    print (f"[{G}*{RE}] Geo-IP Lookup Complete.")
