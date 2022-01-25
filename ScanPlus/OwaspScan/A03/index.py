from ScanPlus.some_function import *
from OwaspScan.A03.SQL_i.index import *
from OwaspScan.A03.XSS_i.index import *
from OwaspScan.A03.Commande_i.index import *

def A03():
    print_blue("Your choice is: \nInjection (A03)\n")

    print_blue("1- SQL Injection")
    print_blue("2- XSS Injection")
    print_blue("3- Commande Injection")
    print()
    choice = input("[ScanPlus] $ choice >> ")

    if choice == "1":
        SQL_i()
    elif choice == "2":
        XSS_i()
    elif choice == "3":
        Commande_i()