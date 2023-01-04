'''

Author: autom4il
Date: 04/01/2023
Website: https://overthewire.org/wargames/natas/
Challenge: Level 7 --> Level 8

'''

#!/usr/bin/env python

import base64
import binascii
import sys

# secret = "3d3d516343746d4d6d6c315669563362"

def decoder(secret):

    string = binascii.unhexlify(secret)[::-1]
    result = base64.b64decode(string).decode("utf-8")

    return result

if __name__ == "__main__":

    input_secret = ""
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " <key>")
    else:
        input_secret = sys.argv[1]

    key = decoder(input_secret)
    print("[+] The secret is: " + key)
