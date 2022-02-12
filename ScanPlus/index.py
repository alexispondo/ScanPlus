#!/usr/bin/python3

from core.some_function import *
from core.global_scan import *
from core.is_bruteforce_scan import *
from core.commonuserpass_scan import *
from core.sqli_scan import *
from core.xssi_scan import *
from core.cmd_i_scan import *

def first_display():
    clear()
    print_yellow("Demarrage ScanPlus...")
    banner()
    print_blue("Quel scan voulez-vous executer ?\n")
    print_blue("1) Scan Global\n")
    print_blue("2) Scan Is_BruteForce\n")
    print_blue("3) Scan CommonUserPass\n")
    print_blue("4) Scan Injection SQL\n")
    print_blue("5) Scan Injection XSS\n")
    print_blue("6) Scan Injection de commande\n")
    print_blue("q) Quitter")
    print("")
    answer = input("scanplus> ")
    return answer


def main():
    answer = first_display()
    while answer != "q":
        if answer == "1":
            global_scan()
        elif answer == "2":
            is_bruteforce()
        elif answer == "3":
            CommonAuth()
        elif answer == "4":
            SQL_i()
        elif answer == "5":
            XSS_i()
        elif answer == "6":
            CMD_i()
        elif answer == "q":
            print("Bye Bye!!!")
            break
        else:
            answer = first_display()


main()
