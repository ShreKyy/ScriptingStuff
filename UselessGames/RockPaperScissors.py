#Crappy Rock Paper Scissors Game Made by ShreKy --> https://github.com/ShreKyy

import random
import time


picks = ["rock", "paper", "scissors"]


def lose():
    print(" ")
    print("You lost!")
    print("""
 _                     
| |                    
| | ___  ___  ___ _ __ 
| |/ _ \/ __|/ _ \ '__|
| | (_) \__ \  __/ |   
|_|\___/|___/\___|_|  
""")
    time.sleep(1)
    print(" ")
    print(f"AI Picked {ai_pick}")
    time.sleep(1)


def win():
    print(" ")
    print("You won!")
    print("""
        _░▒███████
    ░██▓▒░░▒▓██
    ██▓▒░__░▒▓██___██████
    ██▓▒░____░▓███▓__░▒▓██
    ██▓▒░___░▓██▓_____░▒▓██
    ██▓▒░_______________░▒▓██
    _██▓▒░______________░▒▓██
    __██▓▒░____________░▒▓██
    ___██▓▒░__________░▒▓██
    ____██▓▒░________░▒▓██
    _____██▓▒░_____░▒▓██
    ______██▓▒░__░▒▓██
    _______█▓▒░░▒▓██
    ________░▒▓██
    ______░▒▓██
    ____░▒▓██
    """)
    time.sleep(1)
    print(" ")
    print(f"AI Picked {ai_pick}")
    time.sleep(1)


def tie():
    print(" ")
    print("Tie!")
    time.sleep(1)
    print(" ")
    print("Try again...")
    time.sleep(1)


print("Welcome to Rock Paper Scissors!")

while True:
    time.sleep(1)
    pick = input("""
Make your pick...
    
Rock - rock
Paper - paper
Scissors - scissors

""")
    print()
    print("AI is making a pick...")
    ai_pick = random.choice(picks)
    time.sleep(1)
    print(" ")
    print("AI Picked!")
    time.sleep(1)
    print(" ")
    print("Get ready...")
    time.sleep(1)
    if pick.lower() == "rock":
        if ai_pick == "paper":
            lose()

        elif ai_pick == "rock":
            tie()

        elif ai_pick == "scissors":
            win()

    elif pick.lower() == "paper":
        if ai_pick == "paper":
            tie()

        elif ai_pick == "rock":
            win()

        elif ai_pick == "scissors":
            lose()

    if pick.lower() == "scissors":
        if ai_pick == "rock":
            lose()

        elif ai_pick == "paper":
            win()

        elif ai_pick == "scissors":
            tie()
