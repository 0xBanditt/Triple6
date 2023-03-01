-----

<p align="center">
<img src="https://camo.githubusercontent.com/3e24dafd15e0a02df8cf6380ae584d6d190f954c930daac871269eff52a72ce7/68747470733a2f2f692e6962622e636f2f4b713942524e682f696d616765732d31372e6a7067">
</p>

-----

# Triple6 #
Author : [0xBanditt](https://github.com/0xBanditt)

<details>
  <summary>Description</summary>
  <p>An IP look-up tool. Uses APIs for extraction of Information of an IP address. Simple tool nothing else :P</p>
</details>

## Installation ##

```bash
$ pkg install python git 
```
```bash
$ git clone https://github.com/0xBanditt/Triple6
```
```bash 
$ cd Triple6 
```
```bash
$ pip install -r requirements.txt
```
```bash
$ python Triple6.py 
```
* Get your API key from [here](https://www.abuseipdb.com/account/api) (it's free ofc). After getting the API key paste it in `example-config.json`
* Rename `example-config.json` to `config.json`
* simple :white_check_mark:

``` 
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
'$P$$$$$$$$$$$$$$$$$$$$$$$$$$              OSINT tool for IP lookup
 "$c.      4$.  $$       .$$              Type --help or -h for help
  ^$$.      $$ d$"      d$P         Type --commands or -c to show commands
    "$$c.   `$b$F    .d$P"
      `4$$$c.$$$..e$$P"                                                                                             `^^^^^^^`
                    Author   :   0xbanditt
                        GitHub   :   https://github.com/0xBanditt/Triple6
                                                                                                          
# Commands

optional arguments:                                                                                       
-h, --help       show this help message and exi                                                           -c, --commamds   shows command dialog

options:

-n, --nmap       Nmap standard use
-p, --ping       Pings the IP
-nV, --nmap-vuln Uses custom nmap scripts to find vulnerabilities on the system's IP

Example:

python3 Triple6.py --help or -h                         (Display this)
python3 Triple6.py 123.456.789.10 --nmap or -n          (Nmap standard use)
python3 Triple6.py 123.456.789.10                       (Standard use, info about IP)
python3 Triple6.py 123.456.789.10 --ping or -p          (Ping a website or an IP)
python3 Triple6.py 123.456.789.10 --nmap-vuln or -nV    (Uses custom nmap scripts to scan for vulnerabilities on a network)
```
