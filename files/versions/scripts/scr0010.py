import winsound
import time
import psutil
import os
import socket
import GPUtil
from colorama import Fore
def cls():
    os.system('cls')
def write(name):
    with open("u.txt", "w", encoding="utf-8") as f:
        f.write(name)
if os.path.exists("u.txt") and os.path.getsize("u.txt") > 0:
    with open("u.txt", "r", encoding="utf-8") as file:
        name = file.read().strip()
else:
    print("get.username:;")
    time.sleep(0.5)
    print("get.username = err:")
    time.sleep(0.1)
    print("start(), get:")
    time.sleep(0.05)
    print("start - True:")
    time.sleep(0.1)
    print("check.startlist:")
    time.sleep(0.5)
    print("get.all.startlist:")
    time.sleep(0.1)
    print("startlist:\ninput('username')\nafter.input('username')\nlambda.startlist(get(True)))")
    time.sleep(0.1)
    print("lambda: run.startlist.directly = True;")
    time.sleep(0.1)
    cls()
    while True:
        print(Fore.GREEN + "l: " + Fore.WHITE + "enter your username")
        winsound.Beep(1000, 300)
        winsound.Beep(1300, 400)
        name = input(Fore.YELLOW + "lingua: " + Fore.WHITE)
        if name:
            write(name)
            break
        else:
            print(Fore.RED + "err: " + Fore.WHITE + "username not defined")
            winsound.Beep(500, 500)
cls()
print(f"hi, {name}!")
winsound.Beep(1100, 450)
winsound.Beep(1300, 700)
while True:
    version = "0.010"
    cmd = input(Fore.YELLOW +"jungua" + Fore.GREEN + "@" + Fore.WHITE + f"{name}: ")
    winsound.Beep(1500, 200)
    if cmd == 'iam':
        print(name)
    elif cmd.lower() == 'exit':
        break
    elif cmd.lower() == 'fetch':
        disk = psutil.disk_usage('C:\\' if psutil.WINDOWS else '/')
        diskgb = round(disk.total / (1024**3), 2)
        ram = psutil.virtual_memory()
        ramgb = round(ram.total / (1024**3), 2)
        clocker = time.strftime("%Y-%m-%d %H:%M:%S")
        print(Fore.YELLOW + """
             ###########
              #########
              #########
             ###########
              
             ###########
              #########
              #########
              #########
              #########
    ######    #########
   ######## ##########
     ################
        #########
      
""" + Fore.WHITE)
        print(Fore.YELLOW + "version: " + Fore.WHITE + f"{version}\n" + Fore.YELLOW + "disk storage: " + Fore.WHITE + f"{diskgb}GB\n" + Fore.YELLOW + "ram storage: " + Fore.WHITE + f"{ramgb}GB\n" + Fore.YELLOW + "time now: " + Fore.WHITE + f"{clocker}")
    else:
        print(cmd)
