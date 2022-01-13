import pyfiglet


from some_function import *


def banner():
    dev = "Pkaba, Suzou and Sounan"
    print_yellow_bold("@@@@@ ScanPlus By {}  @@@@@@@".format(dev))
    ascii_banner = pyfiglet.figlet_format("Scan Plus")
    print_red_bold(ascii_banner)
    print_blue("ScanPlus is a pentesting program developed by the cybersecurity students at ESATIC ({}),\n"
               "This program allow to scan vulnerability WebSite in following some steps\n"
               "We have two main scan type: Basic scan and Scan based on OWASP Top 10".format(dev))
    print("\n\n\n")


def first_display():
    clear()
    banner()
    print_blue("What SCAN do you wants to do ?\n")
    print_blue("1- Basic Scan")
    print_blue("2- Scan Based On OWASP Top 10")
    print_blue("q- Quit")
    print("")
    answer = input("Your answer number >>")
    return answer


def main():
    answer = first_display()
    while answer != "q":
        if answer == "1":
            print_blue("You have choice global scan")
            main()
        elif answer == "2":
            print_blue("You have choice scan based on OWASP Top 10")
            answer = first_display()
        elif answer == "q":
            break
        else:
            answer = first_display()


main()
