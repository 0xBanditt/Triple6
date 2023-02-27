nmap --version > /dev/null 2>&1
if [ "$?" = "0" ]; then
    exit 1

else
    echo Its important to install nmap, Installing ...
    apt install nmap -y > /dev/null 2>&1

fi
