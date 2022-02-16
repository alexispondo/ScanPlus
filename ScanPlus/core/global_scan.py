import requests
from .some_function import *



######################################################################
## Test if URL is valid
def is_exist(address):
    try:
        req = requests.get(address, headers={"User-Agent": "Mozilla/5.0"})
        if req.status_code in range(200,300) :
            print_green("\n[+] {} existe".format(address))
            return True
        elif req.status_code in range(400,500):
            print_red("\n[-] Votre site web {} n'existe pas".format(address))
            return False
    except (requests.exceptions.MissingSchema, requests.exceptions.InvalidURL) as err:
        print("\nSVP Entrez une url valid: {}".format(str(err)))
    except Exception as err:
        print("\nUne erreure s'est produite: {}".format(str(err)))



######################################################################
## Test if robots.txt file exist
def get_robot(address):
    try:
        add = address + "/robots.txt"
        req = requests.get(add)
        print_blue("\n######### OBTENIR ROBOTS.TXT #########")
        if req.status_code in range(200,300) :
            print_yellow("\n[-] Attention!!!: Le fichier robots.txt a été trouvé ({})".format(add))
            print_yellow(req.text)
        elif req.status_code in range(400,500):
            print_green("\n[+] Super!!!: The File robots.txt n'a pas été trouvé")
        elif req.status_code in range(300,400):
            print_yellow("\n[-] Attention!!!: Vous avez une redirection")
    except Exception as err:
        print(str(err))

######################################################################
## Test if sqlmap.xml.txt file exist
def get_sitemap(address):
    try:
        add = address + "/sitemap.xml"
        req = requests.get(add)
        print_blue("\n######### OBTENIR SITEMAP.XML #########")
        if req.status_code in range(200,300) :
            print_yellow("\n[-] Attention!!!: Le fichier sitemap.xml a été trouvé ({})".format(add))
        elif req.status_code in range(300,400):
            print_yellow("\n[-] Attention!!!: Vous avez une redirection ({})".format(add))
        elif req.status_code in range(400,500):
            print_green("\n[+] Super!!!: Le fichier sitemap.xml n'a pas été trouvé")
    except Exception as err:
        print(str(err))





######################################################################
## Test if sqlmap.xml.txt file exist
def http_https(address):
    try:
        print_blue("\n######### HTTP/HTTPS #########")
        protocol = address.split(":")[0]
        if protocol == "http":
            print_red("\n[-] Danger!!!: Le Hyper Text Transfert Protocol que vous utiliser n'est pas sécurisé. \nUtiliser https:// et non http:// pour crypter la communication")
        elif protocol == "https":
            print_green("\n[+] Super!!!: Vous utiliser un super Hyper Text Transfert Protocol. \nCe https est plus sécurisé")
    except Exception as err:
        print(str(err))


######################################################################
## get programmation language
def prog_lang(address):
    try:
        print_blue("\n######### LANGAGE DE PROGRAMMATION #########")
        req = requests.get(address)
        key_lang = "X-Powered-By"
        if key_lang in req.headers:
            print_yellow("\n[-] Attention!!!: Langage De Programmation Détecté")
            print_yellow("[-] Langage de Programmation: {}".format(req.headers[key_lang]))
        else:
            print_green("\n[+] Super!!!: Le langage de programmation ")
    except Exception as err:
        print(str(err))


######################################################################
## get web server name
def webserver_name(address):
    try:
        print_blue("\n######### NOM ET VERSION DU SERVEUR WEB #########")
        req = requests.get(address)
        key_server= "Server"
        if key_server in req.headers:
            print_yellow("\n[-] Attention!!!: Le Serveur WEB à été détecté")
            print_yellow("[-] Nom du serveur WEB: {}".format(req.headers[key_server]))
        else:
            print_green("\n[+] Super!!!: Le serveur WEB n'a pas été détecté")
    except Exception as err:
        print(str(err))



######################################################################
## Main program of global scan
def global_scan():
    print_blue("\n\n===============================================================================================")
    print_blue("Vous avez choisi Global SCAN")
    print_blue("Ce scan permet de :\n"
               "[*] obtenir robots.txt \n"
               "[*] obtenir sitemap.xml\n"
               "[*] Hyper Text Transfer Protocol est sécurisé où non (http/https) \n"
               "[*] obtenir le langage de programmation\n"
               "[*] Obtenir la version et le nom du serbeur web")

    print("")
    print_blue("[-] Entrez l'adresse url de votre site web. ex: http://127.0.0.1 or https://my_site.com (don't forget http or https)")
    site_addr = input("scanplus> address >> ")
    print()
    if is_exist(site_addr):
        get_robot(site_addr)
        get_sitemap(site_addr)
        http_https(site_addr)
        prog_lang(site_addr)
        webserver_name(site_addr)



