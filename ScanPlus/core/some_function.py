import pyfiglet
from termcolor import colored, cprint
import os
import random


print_blue = lambda x: cprint(x, 'blue')  # Color text on blue
print_red = lambda x: cprint(x, "red")
print_green =  lambda x: cprint(x, "green")
print_yellow = lambda x: cprint(x, "yellow")
print_yellow_bold = lambda x: cprint(x, "yellow", attrs=['bold'])
print_red_bold = lambda x: cprint(x, "red", attrs=['bold'])
clear = lambda: os.system('clear')  # clear terminal

def banner():
    ban1 = """
==============================================================================================================================================
======================================================= ScanPlus =============================================================================
==============================================================================================================================================                                                                                                                                         
                                                                                                                                         
   SSSSSSSSSSSSSSS                                                        PPPPPPPPPPPPPPPPP   lllllll                                    
 SS:::::::::::::::S                                                       P::::::::::::::::P  l:::::l                                    
S:::::SSSSSS::::::S                                                       P::::::PPPPPP:::::P l:::::l                                    
S:::::S     SSSSSSS                                                       PP:::::P     P:::::Pl:::::l                                    
S:::::S                cccccccccccccccc  aaaaaaaaaaaaa  nnnn  nnnnnnnn      P::::P     P:::::P l::::l uuuuuu    uuuuuu      ssssssssss   
S:::::S              cc:::::::::::::::c  a::::::::::::a n:::nn::::::::nn    P::::P     P:::::P l::::l u::::u    u::::u    ss::::::::::s  
 S::::SSSS          c:::::::::::::::::c  aaaaaaaaa:::::an::::::::::::::nn   P::::PPPPPP:::::P  l::::l u::::u    u::::u  ss:::::::::::::s 
  SS::::::SSSSS    c:::::::cccccc:::::c           a::::ann:::::::::::::::n  P:::::::::::::PP   l::::l u::::u    u::::u  s::::::ssss:::::s
    SSS::::::::SS  c::::::c     ccccccc    aaaaaaa:::::a  n:::::nnnn:::::n  P::::PPPPPPPPP     l::::l u::::u    u::::u   s:::::s  ssssss 
       SSSSSS::::S c:::::c               aa::::::::::::a  n::::n    n::::n  P::::P             l::::l u::::u    u::::u     s::::::s      
            S:::::Sc:::::c              a::::aaaa::::::a  n::::n    n::::n  P::::P             l::::l u::::u    u::::u        s::::::s   
            S:::::Sc::::::c     ccccccca::::a    a:::::a  n::::n    n::::n  P::::P             l::::l u:::::uuuu:::::u  ssssss   s:::::s 
SSSSSSS     S:::::Sc:::::::cccccc:::::ca::::a    a:::::a  n::::n    n::::nPP::::::PP          l::::::lu:::::::::::::::uus:::::ssss::::::s
S::::::SSSSSS:::::S c:::::::::::::::::ca:::::aaaa::::::a  n::::n    n::::nP::::::::P          l::::::l u:::::::::::::::us::::::::::::::s 
S:::::::::::::::SS   cc:::::::::::::::c a::::::::::aa:::a n::::n    n::::nP::::::::P          l::::::l  uu::::::::uu:::u s:::::::::::ss  
 SSSSSSSSSSSSSSS       cccccccccccccccc  aaaaaaaaaa  aaaa nnnnnn    nnnnnnPPPPPPPPPP          llllllll    uuuuuuuu  uuuu  sssssssssss    
                                                                                                                                         
Name: ScanPlus                                                                                                                                         
Version: v2.0                                                                                                                                         
Author: @pkaba, @suzou, @sounan                                                                                                                                         
GitHub: https://github.com/alexispondo/ScanPlus

ScanPlus is a pentesting program developed by the cybersecurity students at ESATIC, his program allow to scan vulnerability WebSite in following some steps.
We have two main scan type: Basic scan and Scan based on OWASP Top 10".format(dev)
==============================================================================================================================================
==============================================================================================================================================
==============================================================================================================================================                                                                                                                                         
                                                                                                                                         
                                                                                                                                         

"""
    ban2 = """


  _________                   __________.__                
 /   _____/ ____ _____    ____\______   \  |  __ __  ______
 \_____  \_/ ___\\__  \  /    \|     ___/  | |  |  \/  ___/
 /        \  \___ / __ \|   |  \    |   |  |_|  |  /\___ \ 
/_______  /\___  >____  /___|  /____|   |____/____//____  >
        \/     \/     \/     \/                         \/ 

Name: ScanPlus                                                                                                                                         
Version: v2.0                                                                                                                                         
Author: @pkaba, @suzou, @sounan                                                                                                                                         
GitHub: https://github.com/alexispondo/ScanPlus

ScanPlus is a pentesting program developed by the cybersecurity students at ESATIC, his program allow to scan vulnerability WebSite in following some steps.
We have two main scan type: Basic scan and Scan based on OWASP Top 10".format(dev)

"""

    ban3 = """

 .----------------.  .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |    _______   | || |     ______   | || |      __      | || | ____  _____  | || |   ______     | || |   _____      | || | _____  _____ | || |    _______   | |
| |   /  ___  |  | || |   .' ___  |  | || |     /  \     | || ||_   \|_   _| | || |  |_   __ \   | || |  |_   _|     | || ||_   _||_   _|| || |   /  ___  |  | |
| |  |  (__ \_|  | || |  / .'   \_|  | || |    / /\ \    | || |  |   \ | |   | || |    | |__) |  | || |    | |       | || |  | |    | |  | || |  |  (__ \_|  | |
| |   '.___`-.   | || |  | |         | || |   / ____ \   | || |  | |\ \| |   | || |    |  ___/   | || |    | |   _   | || |  | '    ' |  | || |   '.___`-.   | |
| |  |`\____) |  | || |  \ `.___.'\  | || | _/ /    \ \_ | || | _| |_\   |_  | || |   _| |_      | || |   _| |__/ |  | || |   \ `--' /   | || |  |`\____) |  | |
| |  |_______.'  | || |   `._____.'  | || ||____|  |____|| || ||_____|\____| | || |  |_____|     | || |  |________|  | || |    `.__.'    | || |  |_______.'  | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 

Name: ScanPlus                                                                                                                                         
Version: v2.0                                                                                                                                         
Author: @pkaba, @suzou, @sounan                                                                                                                                         
GitHub: https://github.com/alexispondo/ScanPlus

ScanPlus is a pentesting program developed by the cybersecurity students at ESATIC, his program allow to scan vulnerability WebSite in following some steps.
We have two main scan type: Basic scan and Scan based on OWASP Top 10".format(dev)

"""
    ban = [ban1, ban2, ban3]
    print_yellow_bold(random.choice(ban))