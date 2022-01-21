from ScanPlus.some_function import *
from OwaspScan.A07.BruteForce.index import *
from OwaspScan.A07.CommonAuth.index import *

def A07():
    print_blue("Your choice is: \nIdentification and Authentication Failures (A07)\n")

    print_blue("1- Brute Force attack is it possible ?")
    print_blue("2- Use this platform it common user/pass authentification ?")
    print()
    choice = input("[ScanPlus] $ choice >> ")

    if choice == "1":
        BruteForce()
    elif choice == "2":
        CommonAuth()