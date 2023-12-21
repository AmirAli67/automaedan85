from requests import post
from time import sleep
from random import choice
import datetime
import sys
from colorama import Fore
from os import system


fruit_passport = str(input("Enter Your Fruit Passport: "))


headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 10; SM-A750F Build/QP1A.190711.020)',
    'Host': 'iran.fruitcraft.ir',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'cookie': f'FRUITPASSPORT={fruit_passport}'}


collect_data = "edata=Gk4KXVpRXRJDSEMTfmMXSA%3D%3D"
deposit_data = "edata=Gk4KUEFQQERbUDpPAwkBAVRZRFQ4UB4aWwoEEA5GW05bAlUECgRTQ1JIBVQEUAVdFwhSQAAJCFsDF1BRBVoMBhFJ"



print("\n\n\n")


def collect_gold(data , headers):
    #proxy = {"http" : "http://188.121.103.205:80"}
    collect = post("http://iran.fruitcraft.ir/cards/collectgold",
        data = data,
        headers = headers,
    )


def deposit_to_bank(data , headers):
    deposit = post("http://iran.fruitcraft.ir/player/deposittobank",
        data = data,
        headers = headers,
    )


def start():
    done = 0
    lost = 0
    
    for i in range(400):
        try:
            collect_gold(collect_data , headers)
            if deposit_ask:
                deposit_to_bank(deposit_data , headers)
            done += 1
        except Exception as e:
            print(e)
            lost += 1
        finally:
            sys.stdout.write(f"\r• Gold Mine Done: {Fore.GREEN}{str(done)}{Fore.RESET} --- • Gold Mine Lost: {Fore.RED}{str(lost)}{Fore.RESET} --- • Bank Deposit: {str(deposit_ask)}")
            sys.stdout.flush()
        sleep(maining_time)


system("clear")
power = input('how may is your manner power ? >> ') # قدرت منفعت معدن
capacity = input('how may is your Capacity ? >> ') #ظرفیت معدن
deposit_ask = input('Do you want to deposit money in the bank? (Y or N) >> ') #ذخیره توی بانک؟
deposit_ask = True if deposit_ask.lower() == "y" else False
    

maining_time = int((int(capacity) / (int(power) / 3600)))

print("\n\n\n\n" , 'mine time is >> ', Fore.CYAN , maining_time, Fore.RESET , ' sec' , "\n")



start()

