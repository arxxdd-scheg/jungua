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
        print(Fore.GREEN + "ob: " + Fore.WHITE + "enter your username")
        winsound.Beep(1000, 300)
        winsound.Beep(1300, 400)
        name = input(Fore.YELLOW + "obiton name: " + Fore.WHITE)
        if name:
            write(name)
            break
        else:
            print(Fore.RED + "err: " + Fore.WHITE + "username not defined")
            winsound.Beep(500, 500)
cls()
print(f"WELCOME, {name}!")
winsound.Beep(1100, 450)
winsound.Beep(1300, 700)
while True:
    ver = "0.10"
    cmd = input(Fore.YELLOW +"obiton" + Fore.GREEN + "/" + Fore.WHITE + f"{name}: ")
    winsound.Beep(1500, 200)
    if cmd == 'whoami':
        print(Fore.YELLOW + "USERNAME: " + Fore.WHITE + f"{name}")
    elif cmd.lower() == 'exit':
        print(Fore.RED + "GET OUT" + Fore.WHITE)
        time.sleep(0.2)
        break
    elif cmd.lower() == 'fetch':
        disk = psutil.disk_usage('C:\\' if psutil.WINDOWS else '/')
        diskgb = round(disk.total / (1024**3), 2)
        ram = psutil.virtual_memory()
        ramgb = round(ram.total / (1024**3), 2)
        clocker = time.strftime("%Y-%m-%d %H:%M:%S")
        print(Fore.YELLOW + """                                
                bbbbbbbb            
                b::::::b            
                b::::::b            
                b::::::b            
                 b:::::b            
   ooooooooooo   b:::::bbbbbbbbb    
 oo:::::::::::oo b::::::::::::::bb  
o:::::::::::::::ob::::::::::::::::b 
o:::::ooooo:::::ob:::::bbbbb:::::::b
o::::o     o::::ob:::::b    b::::::b
o::::o     o::::ob:::::b     b:::::b
o::::o     o::::ob:::::b     b:::::b
o::::o     o::::ob:::::b     b:::::b
o:::::ooooo:::::ob:::::bbbbbb::::::b
o:::::::::::::::ob::::::::::::::::b 
 oo:::::::::::oo b:::::::::::::::b  
   ooooooooooo   bbbbbbbbbbbbbbbb   
""" + Fore.WHITE)
        print(Fore.YELLOW + "OBITON\nver: " + Fore.WHITE + f"{ver}\n" + Fore.YELLOW + "DISK: " + Fore.WHITE + f"{diskgb}GB\n" + Fore.YELLOW + "RAM: " + Fore.WHITE + f"{ramgb}GB\n" + Fore.YELLOW + "TIME: " + Fore.WHITE + f"{clocker}")
    elif cmd.lower() == 'clear' or cmd.lower() =='cls':
        cls()
    elif cmd.startswith('text(') and cmd.endswith(')'):
        text = cmd[5:-1]
        print(Fore.GREEN + f"{text}" + Fore.WHITE)
    elif cmd.lower() == 'rename':
        threading.Thread(target=beeep, daemon=True).start()
        newname = input(Fore.GREEN +"RENAME USER: " + Fore.WHITE)
        if not newname:
            print(Fore.RED + "ERROR: " + Fore.WHITE + "username.ndefined")
            winsound.Beep(500, 500)
            continue
        if newname == name:
            print(Fore.YELLOW + "INFO: " + Fore.WHITE + "username.alr")
            winsound.Beep(800, 300)
        else:
            write(newname)
            name = newname
            winsound.Beep(1000, 300)  
            winsound.Beep(1200, 300)
    elif cmd.lower() == 'delete' or cmd.lower() == 'del':
        name = ""
        write(name)
        break
