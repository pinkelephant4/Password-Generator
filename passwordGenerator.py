import random
import string
from xkcdpass import xkcd_password as xp


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


def generateXkcdPass(
    delimiters,
    include_numbers,
    include_special,
    include_cap,
    num_words=6,
    word_len_start=5,
    word_len_end=9,
):
    wordfile = xp.locate_wordfile()
    mywords = xp.generate_wordlist(
        wordfile=wordfile, min_length=word_len_start, max_length=word_len_end
    )
    


print("Welcome to Password Generator")
print("[1] Get XKCD style password \n[2] Get normal password")
choice = int(input("Enter choice: "))


if choice == 1:
    word_len_start = int(
        input("Range of Number of letters in each word of password phrase \nfrom: ")
    )

    word_len_end = int(input("to: "))
    num_words = int(input("Number of words in the password phrase: "))
    print("Enter any special symbols you want to add and press d when done")
    delimiters = []
    sp_char = input()
    if sp_char != "d":
        while sp_char != "d":
            delimiters.append(sp_char)
            sp_char = input()

    # print(delimiters)

    yes_input = ["y", "Y", "yes", "YES"]

    include_numbers = (
        input("Enter y if you want digits in your password: ") in yes_input
    )
    include_cap = (
        input("Enter y if you want a capital letter in your password: ") in yes_input
    )
    include_special = (
        input("Enter y if you want special characters in your password: ") in yes_input
    )

    generateXkcdPass(
        delimiters,
        include_numbers,
        include_special,
        include_cap,
        num_words,
        word_len_start,
        word_len_end,
    )


elif choice == 2:
    yes_input = ["y", "Y", "yes", "YES"]

    length = int(input("Enter minimum length of password required: "))
    include_numbers = (
        input("Enter y if you want digits in your password: ") in yes_input
    )
    include_cap = (
        input("Enter y if you want a capital letter in your password: ") in yes_input
    )
    include_special = (
        input("Enter y if you want special characters in your password: ") in yes_input
    )
    generatePass(length, include_special, include_numbers, include_cap)
