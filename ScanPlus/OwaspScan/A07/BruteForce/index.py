import requests
from ScanPlus.some_function import *
from threading import Thread

def is_bruteforce(url, username = "admin", password = "admin"):
    url = url
    data = {
        username: username,
        password: password
    }
    r = requests.post(url=url, data=data)
    print(r.status_code)
    print(r.headers)
    print()
    #print(r.text)
    #return r.headers

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

    #print("\nEnter the name of your submit parameter. ex: submit")
    #submit = input("[ScanPlus] $ submit >> ")
    for x in range(20):
        Thread(target=is_bruteforce(url, username, password)).start()
