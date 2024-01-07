import random
import string

print("Welcome to Password Generator")

yes_input = ["y", "Y", "yes", "YES"]

length = int(input("Enter minimum password length: "))
include_numbers = input("Enter y if you want digits in your password: ") in yes_input
include_special = (
    input("Enter y if you want special characters in your password: ") in yes_input
)


def generatePass(min_length, special_chars=True, number_chars=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if number_chars:
        characters += digits
    if special_chars:
        characters += special

    pwd = ""
    hasNumber = False
    hasSpecial = False
    criteria_met = False

    while len(pwd) < min_length or not criteria_met:
        newChar = random.choice(characters)
        pwd += newChar

        if newChar in digits:
            hasNumber = True
        elif newChar in special:
            hasSpecial = True


        if special_chars and hasSpecial:
            criteria_met = True
        elif not special_chars and number_chars and hasNumber:
            criteria_met =True
        if number_chars and hasNumber:
            criteria_met = criteria_met and True

    print("Your Password is: ", pwd)


generatePass(length, include_special, include_numbers)
