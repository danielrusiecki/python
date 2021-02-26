import os
import random
import subprocess
from time import sleep
from prettytable import PrettyTable
from datetime import datetime
import webbrowser

url = 'http://10.192.229.231:8000'
available_list = []
busy_list = []
reserved_list = ['10.192.208.100 - "10.192.206.63" Jenkins node',
                 '10.192.208.130 - some other reserved IP']


while True:
    # oryginalnie (range(2, 255), 253)
    for p in random.sample(range(2, 255), 3):
        address = "10.192.208." + str(p)
        if not any(address in x for x in reserved_list):
            res = os.popen("ping -n 1 " + address).read()
            if "TTL=" not in res:
                available_list.append(address)
            else:
                busy_list.append(address)
    print('availeble_list:')
    print(available_list)
    print('busy_list:')
    print(busy_list)

    available_header = 'Available IPs (' + str(len(available_list)) + ')******'
    busy_header = 'Busy IPs (' + str(len(busy_list)) + ')******'
    x = PrettyTable(["LAST UPDATE*********", available_header, busy_header, "RESERVED IPs"])

    # try:
    longer = max(len(available_list), len(busy_list))
    # except:
    #     longer = len(available_list)
    print('wieksza:')
    print(longer)

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # last_update.append(dt_string)
    last_update = [dt_string]

    for i in range(longer):
        try:
            ele1 = available_list[i]
        except:
            ele1 = ''
        try:
            ele2 = busy_list[i]
        except:
            ele2 = ''
        try:
            ele3 = reserved_list[i]
        except:
            ele3 = ''
        try:
            ele4 = last_update[i]
        except:
            ele4 = ''

        x.add_row([ele4, ele1, ele2, ele3])


    refresh_tag = '<head><meta http-equiv="refresh" content="2"></head>'
    wynik = refresh_tag + x.get_html_string()
    print('KOD HTML')
    print(wynik)


    file = open("C:\\Users\\rusiecki\\Desktop\\ind.html", "w")
    file.write(wynik)
    file.close()

    sleep(2)

    available_list = []
    busy_list = []
    # last_update = []

