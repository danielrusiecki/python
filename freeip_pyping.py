import os
import pyping
import pyperclip

start_value = input("Input START value (just last octet of IP address): ")
if start_value in range(1, 256):  
    for x in range(start_value, 256):
        r = pyping.ping("10.192.208." + str(x))
        if r.ret_code == 1:
            print("\nSUCCESS! Free ip address for your new VS has been found!")
            pyperclip.copy("10.192.208." + str(x))
            print(pyperclip.paste() + ' - it has been already COPIED to clipboard, now you can just use CTRL + V \n')
            break
else:
    print("\nERROR! Provided value is not in range 1-255 ! \n")
os.system("pause")
