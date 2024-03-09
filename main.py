import os
import adafruit_ntp
import socketpool
import time
import wifi

def write_secrets(ssid, password):
    with open("secrets.py", "w") as file:
        file.write(f"ssid = '{ssid}'\n")
        file.write(f"password = '{password}'\n")

try:
    from secrets import ssid, password
except:
    print("Run time-cfg for using time command (only wifi boards)")


try:
    wifi.radio.connect(ssid, password)
except:
    pass

while True:
    pool = socketpool.SocketPool(wifi.radio)
    ntp = adafruit_ntp.NTP(pool, tz_offset=2)
    dir = os.getcwd()
    x = input(f"~ [{dir}] > ")

    if x == "ls" or x.startswith("ls "):  
        parts = x.split(" ")  
        if len(parts) > 1:  
            directory = parts[1]  
        else:
            directory = "."  
        try:
            files = os.listdir(directory)  
            for file in files:
                print(file)
        except FileNotFoundError:
            print("Directory not found.")

    elif x.startswith("cd"):
        parts = x.split(" ")
        if len(parts) < 2 or parts[1] == '':
            print("Please specify directory.")
            continue
        directory = parts[1]  
        try:
            os.chdir(directory)  
        except FileNotFoundError:
            print("Directory not found.")
    
    elif x == "":
        pass

    elif x == "pwd":
        print(os.getcwd())

    elif x.startswith("cat"):
        parts = x.split(" ")
        if len(parts) < 2 or parts[1] == '':
            print("Please specify a file.")
            continue
        filename = parts[1]
        try:
            with open(filename, "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("File not found.")
        except PermissionError:
            print("Permission denied.")

    elif x.startswith("mkdir"):
        parts = x.split(" ")
        if len(parts) < 2 or parts[1] == '':
            print("Please specify directory name.")
            continue
        directory = parts[1]
        try:
            os.mkdir(directory)
            print("Directory created successfully.")
        except FileExistsError:
            print("Directory already exists.")

    elif x.startswith("touch"):
        parts = x.split(" ")
        if len(parts) < 2 or parts[1] == '':
            print("Please specify file name.")
            continue
        filename = parts[1]
        try:
            with open(filename, "w") as file:
                pass
            print("File created successfully.")
        except:
            print("Unable to create file.")

    elif x == "fetch":
        system_info = os.uname()
        print("   .~~.   .~~.\n  '. \ ' ' / .'\n   .~ .~~~..~.\n  : .~.'~'.~. :\n ~ (   ) (   ) ~\n( : '~'.~.'~' : )\n ~ .~ (   ) ~. ~\n  (  : '~' :  )\n   '~ .~~~. ~'\n       '~'")
        print("Device:", system_info.machine)
        print("CircuitPython Version:", system_info.version)

    elif x == "time-cfg":
        ssid = input("Enter WiFi SSID: ")
        password = input("Enter WiFi password: ")
        write_secrets(ssid, password)
        print("Configuration saved. Now you need replug your board")

    elif x == "time":
        if ntp.datetime.tm_min < 10:
            print(f"{ntp.datetime.tm_hour}:0{ntp.datetime.tm_min}")
        else:
            print(f"{ntp.datetime.tm_hour}:{ntp.datetime.tm_min}")

    elif x == "help":
        print("List of commands:\nls <directory (optional)> - list of files and directories \ncd <directory> - change directory \npwd - get current path\ncat <filename> - check a file content\nfetch - information about your board\ntime - check what time is now (working only on wifi boards)\ntime-cfg - configure time settings\nhelp - this command")

    else:
        print("Invalid command! Type help for list of commands.")