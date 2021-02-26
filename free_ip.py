import os
import random
import pyperclip

for p in random.sample(range(2, 255), 253):
    address = "10.192.208." + str(p)
    res = os.popen("ping -n 1 " + address).read()
    if "TTL=" in res:
        print(address + " - is UP")
    else:
        print('\nSUCCESS! Free ip address for your new VS has been found!')
        pyperclip.copy(address)
        print(address + " - it has been already COPIED to your clipboard, now you can use CTRL+V \n")
        break
os.system("pause")

