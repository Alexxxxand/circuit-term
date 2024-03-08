import os

while True:
    dir = os.getcwd()
    x = input(f"~ [{dir}] > ")

    if x == "ls" or x.startswith("ls "):  # Проверяем, является ли введенная команда "ls" или начинается с "ls "
        parts = x.split(" ")  # Разделяем строку на части по пробелу
        if len(parts) > 1:  # Если есть указание директории
            directory = parts[1]  # Получаем часть строки после "ls "
        else:
            directory = "."  # Если не указана директория, просматриваем текущую
        try:
            files = os.listdir(directory)  # Получаем список файлов в указанной директории
            for file in files:
                print(file)
        except:
            print("Directory not found.")

    elif x.startswith("cd"):
        parts = x.split(" ")
        if len(parts) < 2 or parts[1] == '':
            print("Please specify directory.")
            continue
        directory = parts[1]  
        try:
            os.chdir(directory)  
        except:
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
        except:
            print("File does not exist or permission denied.")

    elif x.startswith("mkdir"):
        parts = x.split(" ")
        if len(parts) < 2 or parts[1] == '':
            print("Please specify directory name.")
            continue
        directory = parts[1]
        try:
            os.mkdir(directory)
            print("Directory created successfully.")
        except:
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

    elif x == "help":
        print("List of commands:\nls <directory (optional)> - list of files and directories \ncd <directory> - change directory \npwd - get current path\ncat <filename> - check a file content\nhelp - this command")

    else:
        print("Invalid command! Type help for list of commands.")
