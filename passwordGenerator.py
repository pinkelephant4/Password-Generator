import random
import string

print("Welcome to Password Generator")

yes_input = ["y", "Y", "yes", "YES"]

length = int(input("Enter minimum password length: "))
include_numbers = input("Enter y if you want digits in your password: ") in yes_input
include_cap = (
    input("Enter y if you want a capital letter in your password: ") in yes_input
)
include_special = (
    input("Enter y if you want special characters in your password: ") in yes_input
)


def generatePass(min_length, special_chars=True, number_chars=True, cap_chars=True):
    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    characters = lower_letters
    if number_chars:
        characters += digits
    if special_chars:
        characters += special
    if cap_chars:
        characters += upper_letters

    pwd = ""
    hasNumber = False
    hasSpecial = False
    hasCap = False
    criteria_met = False

    while len(pwd) < min_length or not criteria_met:
        newChar = random.choice(characters)
        pwd += newChar

        if newChar in digits:
            hasNumber = True
        elif newChar in special:
            hasSpecial = True
        elif newChar in upper_letters:
            hasCap = True

        criteria_met = True
        if special_chars:
            criteria_met = hasSpecial
        if number_chars:
            criteria_met = criteria_met and hasNumber
        if cap_chars:
            criteria_met = criteria_met and hasCap

    print("Your Password is: ", pwd)


generatePass(length, include_special, include_numbers, include_cap)
