from termcolor import colored, cprint
import os


print_blue = lambda x: cprint(x, 'blue')  # Color text on blue
print_yellow_bold = lambda x: cprint(x, "yellow", attrs=['bold'])
print_red_bold = lambda x: cprint(x, "red", attrs=['bold'])
clear = lambda: os.system('clear')  # clear terminal