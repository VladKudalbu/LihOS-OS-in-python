#system: LihOS

#modules
import time
import random
from turtle import *

#SYSTEM PACKS
TRASH = []
SYSTEM_32 = []
USER_PACK1 = []
USER_PACK2 = []
USER_PACK3 = []
PACKS_LIST = ["PACKS_LIST", "SYSTEM_32", "TRASH", "USER_PACK1", "USER_PACK2", "USER_PACK3"]

#COMMANDS LIST
print("""\n/print >> your text >> your text /
/ check system / PC >> green / yellow / red /
/ paint >> (graphic editor) / 
/ shutdown >> shutdown PC
/ random >> one num >> two num >>> ran num /
/ game_num >> game""")

#Defines
def system_logo():
    print(""" 
────────────────────────────────────────────────────────────────────────
─██████─────────██████████─██████──██████─██████████████─██████████████─
─██░░██─────────██░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██─────────████░░████─██░░██──██░░██─██░░██████░░██─██░░██████████─
─██░░██───────────██░░██───██░░██──██░░██─██░░██──██░░██─██░░██─────────
─██░░██───────────██░░██───██░░██████░░██─██░░██──██░░██─██░░██████████─
─██░░██───────────██░░██───██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─
─██░░██───────────██░░██───██░░██████░░██─██░░██──██░░██─██████████░░██─
─██░░██───────────██░░██───██░░██──██░░██─██░░██──██░░██─────────██░░██─
─██░░██████████─████░░████─██░░██──██░░██─██░░██████░░██─██████████░░██─
─██░░░░░░░░░░██─██░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██████████████─██████████─██████──██████─██████████████─██████████████─
────────────────────────────────────────────────────────────────────────
    """)

#games
def What_is_number():
    print("""
░██╗░░░░░░░██╗██╗░░██╗░█████╗░████████╗██╗██╗░██████╗        ███╗░░██╗██╗░░░██╗███╗░░░███╗██████╗░███████╗██████╗░
░██║░░██╗░░██║██║░░██║██╔══██╗╚══██╔══╝╚█║██║██╔════╝        ████╗░██║██║░░░██║████╗░████║██╔══██╗██╔════╝██╔══██╗
░╚██╗████╗██╔╝███████║███████║░░░██║░░░░╚╝██║╚█████╗░        ██╔██╗██║██║░░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝
░░████╔═████║░██╔══██║██╔══██║░░░██║░░░░░░██║░╚═══██╗        ██║╚████║██║░░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗
░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║░░░██║░░░░░░██║██████╔╝        ██║░╚███║╚██████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝╚═════╝░        ╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
    """)
    number = random.randint(1, 100)
    number_user = int(input("Enter your number >>> "))
    tipes = 0
    while True:
        if (int(number_user) == number):
            print("You Win! tipes:", tipes)
            question = input("repeat? >>> ")
            if question == "YES":
                number = random.randint(1, 100)
                number_user = int(input("Enter your number >>> "))
                tipes = 0
            else:
                break
        elif int(number_user) > number:
            print("number is less!")
            number_user = input("Enter your number >>> ")
            tipes += 1
        elif int(number_user) < number:
            print("number is more!")
            number_user = input("Enter your number >>> ")
            tipes += 1

info = "LihOS 2.0 ver, PC_Name: DESKTOP"

#SYSTEM TERMINAL
TERMINAL = input("\n>>> ")

while True:
    if TERMINAL == "print":
        COM_PRINT = input(">>> ")
        print(">>>", COM_PRINT)
        TERMINAL = input(">>> ")
    elif TERMINAL == "shutdown":
        ris = random.randint(1, 7)
        for TIME_SHUT in range(0, ris):
            time.sleep(1)
            repeat = ""
            repeat += "."
            print(f"IS SHUTDOWN{repeat}")
        break
    elif TERMINAL == "check system":
        system_logo()
        print(info)
        question = input("EDIT? >>> ")
        if question == "YES":
            question1 = input("]What do you to change? >>> ")
            if question1 == "PC_Name":
                PC_NAME = input("]Enter your new name >>> ")
                system_logo()
                info = f"]LihOS 2.0 ver, PC_Name: {PC_NAME}"
                print("Sucess!")
                TERMINAL = input(">>> ")
            else:
                print("]is not parametr founded")
                TERMINAL = input(">>> ")
    elif TERMINAL == "random":
        TERMINAL_NUMBER = int(input(">>> "))
        TERMINAL_NUMBER2 = int(input(">>> "))
        COM_RANDOM = random.randint(TERMINAL_NUMBER, TERMINAL_NUMBER2)
        print(">>> ", COM_RANDOM)
        TERMINAL = input(">>> ")
    #Paint
    elif TERMINAL == "paint":
        PAINT_COMMAND = input("Enter command: ")
        PIXELS_COMMAND = int(input("Enter pixels: "))
        COLOR_COM = input("Enter your color: ")
        if PAINT_COMMAND == "forward":
            forward(PIXELS_COMMAND)
        elif PAINT_COMMAND == "right":
            right(PIXELS_COMMAND)
        elif PAINT_COMMAND == "left":
            left(PIXELS_COMMAND)
        elif PAINT_COMMAND == "clearscreen":
            clearscreen()
        elif PAINT_COMMAND == "Fill":
            begin_fill()
        elif PAINT_COMMAND == "FILLEND":
            end_fill()
        elif PAINT_COMMAND == "color":
            color(COLOR_COM)
    elif TERMINAL == "packs":
            print(PACKS_LIST)
            TERMINAL = input(">>> ")
            if TERMINAL == "USER_PACK1":
                COM_NEW_OBJ = input(">>> ")
                USER_PACK1.append(COM_NEW_OBJ)
            elif TERMINAL == "USER_PACK2":
                COM_NEW_OBJ = input(">>> ")
                USER_PACK2.append(COM_NEW_OBJ)
            elif TERMINAL == "USER_PACK3":
                COM_NEW_OBJ = input(">>> ")
                USER_PACK3.append(COM_NEW_OBJ)
            elif TERMINAL == "SYSTEM_32":
                print("not enough rights to execute the information!")
                TERMINAL = input(">>> ")
            elif TERMINAL == "TRASH":
                COM_NEW_OBJ = input("CLEAR? >>> ")
                if COM_NEW_OBJ == "YES":
                    TRASH.clear()
                    print("Sucess!")
                    TERMINAL = input(">>> ")
                else:
                    TERMINAL = input(">>> ")
    elif TERMINAL == "game_num":
        What_is_number()
    else:
        print("!ERROR! 001")
        TERMINAL = input(">>> ")