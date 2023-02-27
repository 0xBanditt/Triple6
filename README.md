# Triple6 #
Author : [0xBanditt](https://github.com/0xBanditt)

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

## Commands ##

### Examples ###
python3 Triple6.py 123.456.789.10
python3 Triple6.py 123.456.789.10 -n

### Commands ###
python3 Triple6.py --help or -h                         (Display this)
python3 Triple6.py 123.456.789.10 --nmap or -n          (Nmap standard use)
python3 Triple6.py 123.456.789.10                       (Standard use, info about IP)
python3 Triple6.py --commands or -c                     (Display avaliable commands)
python3 Triple6.py 123.456.789.10 --ping or -p             (Ping a website or an IP)
python3 Triple6.py 123.456.789.10 --nmap-vuln or -nV       (Uses custom nmap scripts to scan for vulnerabilities on a network)
