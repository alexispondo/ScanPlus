import requests
from ScanPlus.some_function import *
import os
from threading import Thread

def is_bruteforce(url, username, password):
    userPass = os.getcwd() + "/OwaspScan/A07/BruteForce/userPass.txt"
    with open(userPass, "r") as up:
        liste = up.readlines()
        #print(liste)
        #print(type(liste))
        k = 0
        for l in liste:
            data = l.split("\n")[0]
            user = data.split(":")[0]
            passw = data.split(":")[1]
            #print("user={} & passw={}".format(user, passw))
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
                #print(k)
                if k == 10:
                    print_red("[-] The BruteForce attack is possible because more than 10 connection may be execute")
                    print_red("[-] This site does not have a number of connection limits")
            else:
                print_green("[+] The BruteForce attack isn't possible !!")
                print_green("[+] This site have a number of connection limits")
                break








def BruteForce():
    print_blue("You have choisen BruteForce Attack")

    print("\nEnter your url login ex: https://example.com/login")
    url = input("[ScanPlus] $ url >> ")

    print("\nEnter the name of Username parameter. ex: user")
    username = input("[ScanPlus] $ username >> ")

    #print("\nEnter the name of Email parameter. ex: email")
    #email = input("[ScanPlus] $ email >> ")

    print("\nEnter the name of your password parameter. ex: pass")
    password = input("[ScanPlus] $ password >> ")


    #print("\nEnter the error result. ex: Identifiants invalides.")
    #error = input("[ScanPlus] $ error >> ")

    #print("\nEnter the name of your submit parameter. ex: submit")
    #submit = input("[ScanPlus] $ submit >> ")
    #for x in range(20):
    #    Thread(target=is_bruteforce(url, username, password)).start()
    is_bruteforce(url, username, password)#, error)
