import winsound
import time
import threading
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
def beep():
    winsound.Beep(700, 500)
def beeep():
    winsound.Beep(900, 300)
    winsound.Beep(1300, 300)

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
    version = "0.020"
    cmd = input(Fore.YELLOW +"jungua" + Fore.GREEN + "@" + Fore.WHITE + f"{name}: ")
    winsound.Beep(1500, 200)
    if cmd == 'whoami':
        print(Fore.YELLOW + "your username: " + Fore.WHITE + f"{name}")
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
    elif cmd.lower() == 'clear' or cmd.lower() =='cls':
        cls()
    elif cmd.startswith('say(') and cmd.endswith(')'):
        text = cmd[4:-1]
        print(Fore.GREEN + f"{text}" + Fore.WHITE)
    elif cmd.lower() == 'rename':
        threading.Thread(target=beeep, daemon=True).start()
        newname = input(Fore.GREEN +"rename: " + Fore.WHITE)
        if not newname:
            print(Fore.RED + "err: " + Fore.WHITE + "username not defined")
            winsound.Beep(500, 500)
            continue
        threading.Thread(target=beep, daemon=True).start()
        aquest = input(Fore.RED + "do you really want to rename?\n" + Fore.YELLOW +"before rename: " + Fore.WHITE + f"{name}\n" + Fore.YELLOW + "after rename: " + Fore.WHITE + f"{newname}\n" + Fore.LIGHTBLACK_EX + "(y/n) " + Fore.WHITE)
        if aquest.lower() == 'y':
            if newname == name:
                print(Fore.YELLOW + "info: " + Fore.WHITE + "this is already your name")
                winsound.Beep(800, 300)
                continue
            else:
                write(newname)
                name = newname
                winsound.Beep(1000, 300)  
                winsound.Beep(1200, 300)
        else:
            print(Fore.YELLOW + "rename cancelled" + Fore.WHITE)
            winsound.Beep(600, 300)
            pass
    elif cmd.lower() == "help":
        threading.Thread(target=beep, daemon=True).start()
        print(Fore.RED + "check" + Fore.YELLOW + " 'README.md' " + Fore.RED + "on official repository: " + Fore.LIGHTBLACK_EX + "https://github.com/arxxdd-scheg/jungua" + Fore.WHITE)