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
                    print_red("[-] The BruteForce attack is possible because more than 10 connection may be execute")
                    print_red("[-] This site does not have a number of connection limits")
            else:
                print_green("[+] The BruteForce attack isn't possible !!")
                print_green("[+] This site have a number of connection limits")
                break








def is_bruteforce():
    print_blue("\n\n===============================================================================================")
    print_blue("You have choisen BruteForce Attack")

    print("\nEnter your url login ex: https://example.com/login")
    url = input("scanplus> url >> ")

    print("\nEnter the name of Username parameter. ex: user")
    username = input("scanplus> username >> ")

    print("\nEnter the name of your password parameter. ex: pass")
    password = input("scanplus> password >> ")

    can_i_do_brute_force(url, username, password)
