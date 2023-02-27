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

with open("config.json") as MILF:
    config = json.load(MILF)

def check(syA1):
    print (f"\n[{B}*{RE}] Running Reputation Check Against {R}{syA1}{RE}")

    url = 'https://api.abuseipdb.com/api/v2/check'

    querystring = {
        'ipAddress': syA1,
        'maxAgeInDays': '90'
    }

    headers = {
        'Accept': 'application/json',
        'Key': config['APIkey']
    }

    response = requests.request(method='GET', url=url, headers=headers, params=querystring)
 
    # Formatted output
    decodedResponse = json.loads(response.text)
    
    try:
        errors = [error['detail'] for error in decodedResponse['errors']]
        print ( Fore.RED + "Errors:\n    " + "\n    ".join(errors) + Fore.RESET + "\n\n")
        return 1
    except:
        pass
    
    print ( Fore.WHITE + "Domain: " + json.dumps(decodedResponse ["data"]["domain"]))
    print ( "Hostname: " + json.dumps(decodedResponse ["data"]["hostnames"]))
    print ( "Usage Type: " + json.dumps(decodedResponse ["data"]["usageType"]))
    print ( "Confidence of Abuse: " + json.dumps(decodedResponse ["data"]["abuseConfidenceScore"]))
    print ( "Number Times of Reported: " + json.dumps(decodedResponse ["data"]["totalReports"]))
    print ( "Last Reported: " + json.dumps(decodedResponse ["data"]["lastReportedAt"]))
    print ( "Whitelisted: " + json.dumps(decodedResponse ["data"]["isWhitelisted"]) + "\n")

    #This conditional statement outputs the status of the ip address based on abuse of confidence
    if json.dumps(decodedResponse ["data"]["abuseConfidenceScore"]) == "100":
        print ( Fore.YELLOW + "The IP Address " + sys.argv[1] + " Is Malicious and well known for SSH Bruteforce Attacks" + "\n")
    elif json.dumps(decodedResponse ["data"]["abuseConfidenceScore"]) == "0":
        print ( Fore.GREEN + "The IP Address " + sys.argv[1] + " Is Not Malicious" + "\n")
    elif json.dumps(decodedResponse ["data"]["abuseConfidenceScore"]) < "20":
        print ( "The IP Address " + sys.argv[1] + " Is Probably Not Malicious But Should Be Investigated Further")
    elif json.dumps(decodedResponse ["data"]["abuseConfidenceScore"]) <= "20":
        print ( "The IP Address " + sys.argv[1] + " Is Probably Malicious And Should Be Investigated Further")
    else:
        print (f"{RE}[{G}*{RE}] IP Reputation Look up Complete.")

    print (f"{RE}[{G}*{RE}] IP Reputation Look up Complete.")
    print ( RE )
