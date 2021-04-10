import random
from termcolor import colored
import time
import string

LETTERS = string.ascii_letters
NUMBERS = string.digits  
SPECIAL = string.punctuation  


def passwd_length():
      length = input(colored("Password length: ", "green"))
      return int(length)

def pass_combination():
      letters = input(colored("Letters? (True,False) ", "green"))
      digits = input(colored("Digits? (True,False) ", "green"))
      special_chars = input(colored("Special chars? (True,False) ", "green"))
      letters = eval(letters.title())
      digits = eval(digits.title())
      special_chars = eval(special_chars.title())

      try:
            return [digits, letters, special_chars]

      except NameError as e:
        print("Invalid value. Use either True or False")
        print("Invalidity returns a default, try again to regenerate")

      return [True, True, True]


def generate_pass(cbl, length=8):
      printable = strings_constant(cbl)
      printable = list(printable)
      random.shuffle(printable)
      password = random.choices(printable, k=length)
      password = "".join(password)
      return password

def strings_constant(choice_list):
      strings_constant = ""
      strings_constant += NUMBERS if choice_list[0] else ""
      strings_constant += LETTERS if choice_list[1] else ""
      strings_constant += SPECIAL if choice_list[2] else ""
      
      return strings_constant

if __name__ == "__main__":
      length = passwd_length()
      choice_list = pass_combination()
      password = generate_pass(choice_list, length)
      print(colored("Generating password...", "red"))
      print()
      time.sleep(1)
      print(colored(f"Your password: {password}", "green"))
