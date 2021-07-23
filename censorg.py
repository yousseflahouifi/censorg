import censys.ipv4
import censys.certificates
import argparse

UID = "***"
SECRET = "***"


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("orgname",help="the organization name")
    parser.add_argument("-d","--domains",help="retreive hostnames with the same organization field in a SSL certificate",action='store_true')
    parser.add_argument("-i","--ip",help="Retreive ips with the same organization field in a SSL certificate",action='store_true')
    return parser.parse_args()


def banner():
    print("""
 ___ ___ _ __  ___  ___  _ __ __ _ 
  / __/ _ \ '_ \/ __|/ _ \| '__/ _` |
 | (_|  __/ | | \__ \ (_) | | | (_| |
  \___\___|_| |_|___/\___/|_|  \__, |
                                __/ |
                               |___/
     By Youssef Lahouifi

    """)
def get_domains(orgname):

    certificates = censys.certificates.CensysCertificates(UID, SECRET)
    fields = ["parsed.extensions.subject_alt_name.dns_names", "parsed.subject.common_name"]

    search = 'parsed.subject.organization:'+orgname

    for c in certificates.search(search, fields=fields,max_records=1000):
        print(c["parsed.subject.common_name"][0])
        try:
            if(len(c["parsed.extensions.subject_alt_name.dns_names"])>1):
                for i in range(len(c["parsed.extensions.subject_alt_name.dns_names"])):
                    print(c["parsed.extensions.subject_alt_name.dns_names"][i])
            else:
                print(c["parsed.extensions.subject_alt_name.dns_names"][0])
        except(KeyError,KeyboardInterrupt):
            pass


def get_hosts(orgname):

    c = censys.ipv4.CensysIPv4(UID, SECRET)

    search = "443.https.tls.certificate.parsed.subject.organization:"+orgname

    for result in c.search(search, max_records=1000):
        print(result['ip'])


if __name__ == '__main__':
    banner()
    orgname=args().orgname
    if args().domains:
        print("[+] Retrieving the hostnames that have SSL certificate with organization : "+orgname)
        get_domains(orgname)
    if args().ip:
        print("[+] Retrieving the hosts that have SSL certificate with organization : "+orgname)
        get_hosts(orgname)

