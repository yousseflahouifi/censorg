# What's this tool about ?
Finding hosts or domain names associated with a company where the domain name does not include the name of the company can sometimes be difficult.  There are common ways to do it such ASN, reverse ip lookup etc.  
Censorg is a security reconnaissance tool that leverage Censys API to look for domains and hosts with the same Organization field in the SSL certificate.

# Recommended python version :
Python 3.x.

# installation :
```
git clone https://github.com/yousseflahouifi/censorg.git
```

# Dependencies :
Censorg depends on the censys and argparse python modules :
* install argparse :
```
pip install argparse
```
* Install censys
```
pip install censys
```
* install requests :
```
pip install requests
```

# Setup :
Censorg uses the Censys API to look for domains and ips with the same Organization field in the SSL certificate, so you will need to get keys from censys and set both UID and SECRET variable in the script (use whatever editor you like) .

# Usage :
```
usage: censorg.py [-h] [-d] [-i] orgname
```
| Short form | Long form | Description |
| :---         |  :---         |  :---         |
| -h   | --help     | Show help message and exit    |
| -d     | --domains       | retreive hostnames with the same organization field in a SSL certificate      |
| -i     | --ip       | retreive ips with the same organization field in a SSL certificate      |

# Example :

```
python3 censorg.py "LLC Mail.Ru" -i

 ___ ___ _ __  ___  ___  _ __ __ _ 
  / __/ _ \ '_ \/ __|/ _ \| '__/ _` |
 | (_|  __/ | | \__ \ (_) | | | (_| |
  \___\___|_| |_|___/\___/|_|  \__, |
                                __/ |
                               |___/
     By Youssef Lahouifi

    
[+] Retrieving the hosts that have SSL certificate with organization : LLC Mail.Ru
217.69.137.46
217.69.136.88
185.5.139.102
217.69.143.7
185.5.139.33
217.69.136.114
217.69.138.111
217.69.139.25
185.5.139.56
128.140.169.70
```
# Notes :
Censorg shows only the first 1000 result in censys as i am using a regular community subscription . If you have upgraded one use a text editor and look for the value 1000 and change it to whatever you like .
