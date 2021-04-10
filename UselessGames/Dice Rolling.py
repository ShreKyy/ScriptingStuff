import random
import time
from termcolor import colored,cprint

print(colored("Hello and welcome to this dice rolling simulator", "yellow"))

flag_roll = True

time.sleep(2)

while flag_roll:
   roll = input(colored("""
Enter the commands below to do an action:
   
Roll the dice - roll
Exit out of the program - quit
   
""", "green"))

   if roll.lower() == "roll":
      reroll = True
      if reroll:
         number = random.randint(1, 6)
         print(" ")
         while reroll:
            print(colored("Rolling the dice...", "yellow", "on_grey"))
            print(" ")
            time.sleep(1)
            print(colored(f"You rolled a","green",),end=" ")
            print(colored(f"{number}", "red"))
            time.sleep(2)
            print(" ")
            choice = input(colored("""
Would you like to roll again?
Yes - yes
No,exit the game - no

""", "yellow"))

            if choice.lower() == "yes":
               print(" ")
               reroll = True

            elif choice.lower() == "no":
               print(" ")
               print(colored("Ok bye lol", "red"))
               time.sleep(1)
               exit()

            else:
               print(" ")
               print(colored("tf u saying dude,I don't understand that,try again", "red"))
               print(" ")
               time.sleep(1)
               flag_roll = True

   elif roll.lower() == "quit":
      flag_roll = False
      print(" ")
      print(colored("Ok bye lol", "red"))
      time.sleep(1)
      exit()

   else:
      print(" ")
      print(colored("tf u saying dude,I don't understand that,try again", "red"))
      print(" ")
      time.sleep(1)
      flag_roll = True
