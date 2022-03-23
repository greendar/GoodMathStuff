import os
import random

def clear():
    os.system("cls")

options = """
    1. Print Some Numbers
    2. Clear Screen
    0. Exit Program

    """


notDone = True

while notDone:
    print(options)
    choice = input("What would you like to do?\n: ")
    if choice == '1':
        for i in range(100):
            r = random.randint(1, 10000)
            print(chr(r), end="")
        print()
    elif choice == '2':
        clear()
    elif choice == '0':
        break

print("Program is complete.")
