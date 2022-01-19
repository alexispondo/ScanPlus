import requests

from ScanPlus.some_function import *
#from ScanPlus.index import main as main_index

######################################################################
## Test if URL is valid
def is_exist(address):
    try:
        req = requests.get(address)
        if req.status_code in range(200,300) :
            print_green("\n[+] {} exist".format(address))
            return True
        elif req.status_code in range(400,500):
            print_red("\n[-] Your web site {} not exist".format(address))
            return False
    except (requests.exceptions.MissingSchema, requests.exceptions.InvalidURL) as err:
        print("\nPlease enter a valid URL: {}".format(str(err)))
    except Exception as err:
        print("\nOne error is product: {}".format(str(err)))



######################################################################
## Test if robots.txt file exist
def get_robot(address):
    try:
        add = address + "/robots.txt"
        req = requests.get(add)
        print_blue("\n######### GET ROBOTS.TXT #########")
        if req.status_code in range(200,300) :
            print_yellow("\n[-] Warning!!!: The File robots.txt is found ({})".format(add))
            print_yellow(req.text)
        elif req.status_code in range(400,500):
            print_green("\n[+] Great!!!: The File robots.txt is not found")
        elif req.status_code in range(300,400):
            print_yellow("\n[-] Warning!!!: we have a redirection")
    except Exception as err:
        print(str(err))

######################################################################
## Test if sqlmap.xml.txt file exist
def get_sitemap(address):
    try:
        add = address + "/sitemap.xml"
        req = requests.get(add)
        print_blue("\n######### GET SITEMAP.XML #########")
        if req.status_code in range(200,300) :
            print_yellow("\n[-] Warning!!!: The File sitemap.xml is found ({})".format(add))
        elif req.status_code in range(300,400):
            print_yellow("\n[-] Warning!!!: we have a redirection ({})".format(add))
        elif req.status_code in range(400,500):
            print_green("\n[+] Great!!!: The File sitemap.xml is not found")
    except Exception as err:
        print(str(err))





######################################################################
## Test if sqlmap.xml.txt file exist
def http_https(address):
    try:
        print_blue("\n######### HTTP/HTTPS #########")
        protocol = address.split(":")[0]
        if protocol == "http":
            print_red("\n[-] Danger!!!: The Hyper Text Transfert Protocol that you use is not secure. \nUse https:// and not http:// for crypte your communication")
        elif protocol == "https":
            print_green("\n[+] Great!!!: You use the great Hyper Text Transfert Protocol. \nThis https is more secure")
    except Exception as err:
        print(str(err))


######################################################################
## get programmation language
def prog_lang(address):
    try:
        print_blue("\n######### PROGRAMMATION LANGUAGE #########")
        req = requests.get(address)
        key_lang = "X-Powered-By"
        if key_lang in req.headers:
            print_yellow("\n[-] Warning!!!: Programmation language detected")
            print_yellow("[-] Programmation Language: {}".format(req.headers[key_lang]))
        else:
            print_green("\n[+] Great!!!: Your programing language is not display")
    except Exception as err:
        print(str(err))


######################################################################
## get web server name
def webserver_name(address):
    try:
        print_blue("\n######### WEB SERVER NAME #########")
        req = requests.get(address)
        key_server= "Server"
        if key_server in req.headers:
            print_yellow("\n[-] Warning!!!: Web Server Name Detected")
            print_yellow("[-] Web Server Name: {}".format(req.headers[key_server]))
        else:
            print_green("\n[+] Great!!!: Your Web Server Name is not display is not display")
    except Exception as err:
        print(str(err))



######################################################################
## Main program of global scan
def display_global():
    #clear()
    #banner()
    print_blue("You have chosen Global Scan")
    print_blue("This Scan allow to :\n"
               "[*] get robots.txt \n"
               "[*] get sitemap.xml\n"
               "[*] secure or not secure Hyper Text Transfer Protocol (http/https) \n"
               "[*] get programmation language\n"
               "[*] get WebServer name and version\n"
               "[*] list vulnerability of this version and get the version which fix it")

    print("")
    print_blue("[-] Enter your web site address. ex: http://127.0.0.1 or https://my_site.com (don't forget http or https)")
    site_addr = input("[ScanPlus] $ address >> ")
    print()
    if is_exist(site_addr):
        get_robot(site_addr)
        get_sitemap(site_addr)
        http_https(site_addr)
        prog_lang(site_addr)
        webserver_name(site_addr)
    #main_index()



