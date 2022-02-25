import random
from colorama import Fore, Style
import os
from os import system
import pyperclip

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
    print(Style.RESET_ALL)

def toggle(var):
    if var == True:
        return False
    elif var == False:
        return True
    elif var == 1:
        return 0
    elif var == 0:
        return 1

class password:

    listcaps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    listchars = "abcdefghijklmnopqrstuvwxyz"
    listdigits = "1234567890"
    listsimbols = "#@*$%?!€.,:;"
    possibility = ["0","1","2","3","4","5", "author"]

    caps = True
    chars = True
    digits = False
    simbols = True
    lenght = 8

    class isVar:
        def caps():
            if password.caps == True:
                return Fore.LIGHTGREEN_EX + "[1] uppercase"
            else:
                return Fore.LIGHTBLACK_EX + "[1] uppercase"
        def chars():
            if password.chars == True:
                return Fore.LIGHTGREEN_EX + "[2] characters"
            else:
                return Fore.LIGHTBLACK_EX + "[2] charatcters"
        def digits():
            if password.digits == True:
                return Fore.LIGHTGREEN_EX + "[3] digits"
            else:
                return Fore.LIGHTBLACK_EX + "[3] digits"
        def simbols():
            if password.simbols == True:
                return Fore.LIGHTGREEN_EX + "[4] simbols"
            else:
                return Fore.LIGHTBLACK_EX + "[4] simbols"

    def generate(caps, chars, digits, simbols, lenght):
        
        all = ""
        psw = ""

        if caps == True:
            all = all + password.listcaps
        if chars == True:
            all = all + password.listchars
        if digits == True:
            all = all + password.listdigits
        if simbols == True:
            all = all + password.listsimbols
        if all == "":
            return Fore.RED + "Error - you have to select at least one of these options: uppercase, character, digits, simbols"

        for _ in range(lenght):
            psw += random.choice(all)
        
        pyperclip.copy(psw)
        return psw

    def set_lenght():
        clearConsole()
        lenght = input(Fore.BLUE + "Enter the lengt of the password: ")
        try:
            lenght = int(lenght)
            return lenght
        except Exception as e:
            password.set_lenght()

    def send_author():
        clearConsole()
        print(Fore.LIGHTCYAN_EX+"==================================")
        print("")
        print("Script made by Juro")
        print(Style.RESET_ALL)
        print("Discord        Juro#1710")
        print("Github         juro0")
        print("Telegram       @juri_gemignani")
        print("Web site:      juro0.github.io")
        print("IG/twitter     @juri_gemignani")
        print(Fore.LIGHTCYAN_EX+"==================================")
        print(Fore.LIGHTBLACK_EX)
        input("click to return... ")

    def send_home():
        title = "Password Generator - UI"
        system("title "+title)
        clearConsole()
        print(Fore.CYAN + "==================== PASSWORD GENERATOR - Juro ====================")
        print(Style.RESET_ALL)
        print(f"{password.isVar.caps()}    {password.isVar.chars()}")
        print(f"{password.isVar.digits()}       {password.isVar.simbols()}")
        print(Style.RESET_ALL)
        print("[5] lenght       [0] generate")
        print("")
        print(Fore.BLUE)
        choice = input("> ")
        
        if choice in password.possibility:
            pass
        else:
            password.send_home()
        
        if choice == "1":
            password.caps = toggle(password.caps)
        if choice == "2":
            password.chars = toggle(password.chars)
        if choice == "3":
            password.digits = toggle(password.digits)
        if choice == "4":
            password.simbols = toggle(password.simbols)
        if choice == "5":
            password.lenght = password.set_lenght()
            password.isLenght = True
        if choice == "0":
            print(Fore.CYAN)
            print(password.generate(password.caps, password.chars, password.digits, password.simbols, password.lenght) )
            print("")
            print("password successfully copied to clipboard. Press ctrl+v (or cmd+v) if you want to use it!")
            print(Style.RESET_ALL)
            input("Press enter... ")
            password.send_home()
        if choice == "author":
            password.send_author()
        password.send_home()

password.send_home()