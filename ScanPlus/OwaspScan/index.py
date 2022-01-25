import requests

from ScanPlus.some_function import *
from OwaspScan.A07.index import *
from OwaspScan.A03.index import *
#from ScanPlus.index import main as main_index




######################################################################
## Main program of global scan
def display_owasp():
    #clear()
    #banner()
    print_blue("You have chosen Scan based OWASP")
    print_blue("This Scan allow to test if your web site contain a vulnerability list on OWASP TOP10:\n")
    print_blue("\nTake your choice:")
    print_blue("1- Broken Access Control (A01)")
    print_blue("2- Cryptographic Failures (A02)")
    print_blue("3- Injection (A03)")
    print_blue("4- Insecure Design (A04)")
    print_blue("5- Security Misconfiguration (A05)")
    print_blue("6- Vulnerable and Outdated Components (A06)")
    print_blue("7- Identification and Authentication Failures (A07)")
    print_blue("8- Software and Data Integrity Failures (A08)")
    print_blue("9- Security Logging and Monitoring Failures (A09)")
    print_blue("10- Server Side Request Forgery (SSRF) (A10)")
    print()
    choice = input("[ScanPlus] $ choice >> ")

    if choice == "1":
        #A01()
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        A03()
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        pass
    elif choice == "7":
        A07()
    elif choice == "8":
        pass
    elif choice == "9":
        pass
    elif choice == "10":
        pass
