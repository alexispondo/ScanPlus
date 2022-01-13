import pyfiglet
from termcolor import colored, cprint
import os


print_blue = lambda x: cprint(x, 'blue')  # Color text on blue
print_red = lambda x: cprint(x, "red")
print_green =  lambda x: cprint(x, "green")
print_yellow = lambda x: cprint(x, "yellow")
print_yellow_bold = lambda x: cprint(x, "yellow", attrs=['bold'])
print_red_bold = lambda x: cprint(x, "red", attrs=['bold'])
clear = lambda: os.system('clear')  # clear terminal

def banner():
    dev = "Pkaba, Suzou and Sounan"
    print_yellow_bold("@@@@@ ScanPlus By {}  @@@@@@@".format(dev))
    ascii_banner = pyfiglet.figlet_format("Scan Plus")
    print_red_bold(ascii_banner)
    print_blue("ScanPlus is a pentesting program developed by the cybersecurity students at ESATIC ({}),\n"
               "This program allow to scan vulnerability WebSite in following some steps\n"
               "We have two main scan type: Basic scan and Scan based on OWASP Top 10".format(dev))
    print("\n\n\n")