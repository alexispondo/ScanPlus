import requests
from .some_function import *
import os

def can_i_do_brute_force(url, username, password):
    userPass = os.getcwd() + "/core/wordlist/is_bruteforce.txt"
    with open(userPass, "r") as up:
        liste = up.readlines()
        k = 0
        for l in liste:
            data = l.split("\n")[0]
            user = data.split(":")[0]
            passw = data.split(":")[1]
            headers = {'User-Agent': 'Mozilla/5.0'}
            payload = {username: user, password: passw}
            link = url
            session = requests.Session()
            try:
                resp = session.get(link, headers=headers)
            except Exception as e:
                print(e)
            cookies = requests.utils.cookiejar_from_dict(requests.utils.dict_from_cookiejar(session.cookies))
            try:
                resp = session.post(link, headers=headers, data=payload, cookies=cookies)
            except Exception as e:
                print(e)

            if resp.status_code == 200:
                k = k + 1
                print_green("{} ".format(k))
                if k == 10:
                    print_red("[-] L'attaque brutefoce est possible car plus de 10 connexions échouées ont été exécuté")
                    print_red("[-] Ce site n'a pas de nombre de connexion limité")
            else:
                print_green("[+] L'attaque bruteforce n'est pas possible !!")
                print_green("[+] Ce site a un nombre de connexion limité")
                break








def is_bruteforce():
    print_blue("\n\n===============================================================================================")
    print_blue("Vous avez choisi le scan is_bruteforce qui vérifie si l'attaque bruteforce est possible")

    print("\nEntrez l'url de la page de connexion ex: https://example.com/login")
    url = input("scanplus> url >> ")

    print("\nEntrez le nom de l'input username. ex: user")
    username = input("scanplus> username >> ")

    print("\nEntrez le nom de l'input password. ex: pass")
    password = input("scanplus> password >> ")

    can_i_do_brute_force(url, username, password)
