
# à executer dabord
# export PYTHONPATH="${PYTHONPATH}:/home/alexispondo/projet_pi/"
from some_function import *
from GlobalScan.index import *
from OwaspScan.index import *

def first_display():
    clear()
    banner()
    print_blue("What SCAN do you wants to do ?\n")
    print_blue("1- Basic Scan")
    print_blue("2- Scan Based On OWASP Top 10")
    print_blue("q- Quit")
    print("")
    answer = input("ScanPlus $ Your answer number >> ")
    return answer


def main():
    answer = first_display()
    while answer != "q":
        if answer == "1":
            display_global()
        elif answer == "2":
            print_blue("You have choice scan based on OWASP Top 10")
            answer = display_owasp()
        elif answer == "q":
            break
        else:
            answer = first_display()


main()
