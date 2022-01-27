import requests
from .some_function import *
import os



def test_if_user_and_passw_are_good(url, username, password, submit, error):
    userPass = os.getcwd() + "/core/wordlist/commonuserpass.txt"
    with open(userPass, "r") as up:
        liste = up.readlines()
        k = 0
        for l in liste:
            data = l.split("\n")[0]
            user = data.split(":")[0]
            passw = data.split(":")[1]
            headers = {'User-Agent': 'Mozilla/5.0'}
            payload = {username: user, password: passw, submit: "Ok"}
            link = url
            session = requests.Session()
            try:
                resp = session.get(link, headers=headers)
            except Exception as e:
                print(e)
            cookies = requests.utils.cookiejar_from_dict(requests.utils.dict_from_cookiejar(session.cookies))
            #print(cookies)
            try:
                resp = session.post(link, headers=headers, data=payload, cookies=cookies)
            except Exception as e:
                print(e)
            #print(resp.headers)
            if resp.status_code == 200:
                k = k + 1
                if error in resp.text:
                    print_red_bold("login-{} : username = {} || password = {} =====>>>>> Username or Password Incorrect".format(k, user, passw))
                else:
                    print_green("login-{} : username = {} || password = {} =====>>>>> Correct Username and Password".format(k, user, passw))
                    break
            else:
                print_green("Vérifiez vos paramètres de connexion")
                break








def CommonAuth():
    print_blue("\n\n===============================================================================================")
    print_blue("Vous avez choisi le scan des informations d'identification commune")

    print("\nEntrez l'URL de la page de connexion ex: https://example.com/login")
    url = input("scanplus> url >> ")

    print("\nEntrez le nom de l'input username. ex: user")
    username = input("scanplus> username >> ")

    print("\nEntrez le nom de l'input password. ex: pass")
    password = input("scanplus> password >> ")


    print("\nEntrez le message d'erreur. ex: Identifiants invalides.")
    error = input("scanplus> error >> ")

    print("\nEntrez le nom du bouton d'envoi. ex: submit")
    submit = input("scanplus> submit >> ")

    test_if_user_and_passw_are_good(url, username, password, submit, error)
