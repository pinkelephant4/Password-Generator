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
    include_cap,
    acronym,
    num_words=6,
    word_len_start=5,
    word_len_end=9,
):
    wordfile = xp.locate_wordfile()
    mywords = xp.generate_wordlist(
        wordfile=wordfile, min_length=word_len_start, max_length=word_len_end
    )

    if acronym != "":
        word_v1 = xp.generate_xkcdpassword(wordlist=mywords, acrostic=acronym)
    else:
        word_v1 = xp.generate_xkcdpassword(wordlist=mywords, numwords=num_words)
    joined_str = word_v1.replace(" ", "")
    word_v1 = str.split(word_v1)

    if include_cap:
        iterations = random.randrange(len(joined_str) - 1)
        for index in range(iterations):
            i = random.randrange(len(word_v1))
            j = random.randrange(len(word_v1[i]))
            chosen_word = word_v1[i]
            chosen_word = (
                chosen_word[:j] + chosen_word[j].upper() + chosen_word[j + 1 :]
            )
            word_v1[i] = chosen_word

    if include_numbers:
        iterations = random.randrange(len(joined_str) // 3)
        for index in range(iterations):
            i = random.randrange(len(word_v1))
            j = random.randrange(len(word_v1[i]))
            chosen_word = word_v1[i]
            chosen_word = chosen_word[:j] + str(random.randint(0, 9)) + chosen_word[j:]
            word_v1[i] = chosen_word

    new_password = ""

    for i in range(len(word_v1)):
        index = random.randrange(len(delimiters))

        rand_delim = delimiters[index - 1]

        joining_words = str(word_v1[i]) + str(rand_delim)

        new_password = new_password + joining_words

    print(new_password)


print("Welcome to Password Generator")
print("[1] Get XKCD style password \n[2] Get normal password")

choice = input("Enter choice: ")
while not choice.isdigit() or int(choice) not in [1, 2]:
    print("\n\nPls enter valid choice ")
    print("[1] Get XKCD style password \n[2] Get normal password")
    choice = input("Enter choice: ")
choice = int(choice)

yes_input = ["y", "Y", "yes", "YES"]


if choice == 1:
    # try:
    #     word_len_start = int(
    #         input("Range of Number of letters in each word of password phrase \nfrom: ")
    #     )
    # except ValueError:
    #     print("Pls enter a valid start of range: ")
    #     word_len_start = int(
    #         input("Range of Number of letters in each word of password phrase \nfrom: ")
    #     )

    word_len_start = input(
        "Range of Number of letters in each word of password phrase \nfrom: "
    )
    while word_len_start == "0" or not word_len_start.isdigit():
        print("Pls enter a valid start of range: ")
        word_len_start = input(
            "Range of Number of letters in each word of password phrase \nfrom: "
        )

    word_len_start = int(word_len_start)

    word_len_end = input("to: ")
    while not word_len_end.isdigit() or int(word_len_end) <= int(word_len_start):
        print("Pls enter valid value")
        word_len_end = input("to: ")

    word_len_end = int(word_len_end)

    num_words = input("Number of words in the password phrase: ")
    while not num_words.isdigit():
        print("Pls enter a valid value for number of words.")
        num_words = input("Number of words in the password phrase: ")

    num_words = int(num_words)

    include_special = (
        input("Enter y if you want special characters in your password: ") in yes_input
    )

    if include_special:
        special_characters = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        spl = []
        print("Enter special symbols you want to add and press d when done")
        delimiters = []
        sp_char = input()
        if sp_char not in special_characters:
            while sp_char not in special_characters and sp_char != "d":
                print("Pls enter a valid special character.")
                sp_char = input()
        if sp_char != "d":
            while sp_char != "d":
                delimiters.append(sp_char)
                sp_char = input()
                if sp_char not in special_characters and sp_char != "d":
                    while sp_char not in special_characters:
                        print("Pls enter a valid special character.")
                        sp_char = input()
        else:
            delimiters = [" "]
        # print(delimiters)

    else:
        delimiters = [" "]

    include_numbers = (
        input("Enter y if you want digits in your password: ") in yes_input
    )

    include_cap = (
        input("Enter y if you want a capital letter in your password: ") in yes_input
    )

    include_acronym = (
        input("Enter y if you want an acronym for your password: ") in yes_input
    )
    if include_acronym:
        acronym = input("Enter acronym for the passphrase (1 word): ").lower()
        while len(str.split(acronym)) != 1:
            print("Enter valid acronym.")
            acronym = input("Enter acronym for the passphrase (1 word): ").lower()
    else:
        acronym = ""

    generateXkcdPass(
        delimiters,
        include_numbers,
        include_cap,
        acronym,
        num_words,
        word_len_start,
        word_len_end,
    )


elif choice == 2:
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
