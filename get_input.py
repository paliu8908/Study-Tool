from idlelib.configdialog import is_int
import pandas as pd

# get_bool(prompt) prints a prompt and asks
# the user to answer yes or no.
# Returns true if the user answers yes, y, sure, or true

# get_bool: Str -> Bool

def get_bool(prompt):
    bool = False

    confirm_str = ["yes", "y", "sure", "true"]
    ans = ""

    ans = input(prompt).lower()

    for i in range(len(confirm_str)):
        if not ans.find((confirm_str[i])) == -1:
            bool = True
            i = len(confirm_str)

    return bool

# get_int(prompt) prints a prompt and asks
# the user for an integer until an integer is given

# get_int: Str -> Int

def get_int(prompt) :
    value = input(prompt)

    while not value.isdigit():
        print("Error: Not an Integer")
        value = input(prompt)

    value = int(value)

    return value

# get_int_range(prompt, min, max) prints a prompt and asks
# the user for an integer between max and min until a valid
# integer is given.


# get_int_range : Str Int Int -> Int
def get_int_range(prompt, min, max):
    valid = False

    value = input(prompt)

    if not value.isdigit():
        print("Error: Not an Integer")


    elif int(value) < min:
        print("Error: Too small. Must be greater than " + str(min))

    elif int(value) > max:
        print("Error: Too larger. Must be less than " + str(max))

    else:
        valid = True

    while not valid:

        value = input(prompt)

        if not value.isdigit():
            print("Error: Not an Integer")
        elif int(value) < min:
            print("Error: Too small. Must be greater than " + str(min))

        elif int(value) > max:
            print("Error: Too larger. Must be less than " + str(max))

        else:
            valid = True

    value = int(value)

    return value

def get_deck():
    deck_list_path = 'files.csv'
    deck_path = ''
    min_index = 0
    prompt = ""
    choice = -1
    tab_length = 5

    deck_name = ""

    decks_df = pd.read_csv(deck_list_path)

    prompt = "\nOpen a Deck to edit: "
    prompt += "\n0. Go back 1 page."

    for i in range(min_index, min(min_index + tab_length, len(decks_df.index), )):
        prompt += "\n " + str(i + 1) + ". " + decks_df.at[i, 'name'].replace(".csv", "")

    prompt += "\n6. Go forward 1 page."
    prompt += "\n7. Back"

    choice = get_int_range(prompt + "\nChoice: ", 0, tab_length + 2)

    # fix some bugs so that choices are 1 to 5
    while choice < 1 or choice > tab_length:

        if choice == 0:
            prompt = "\nOpen a Deck to edit: "

            min_index = max(0, min_index - tab_length)

            for i in range(min(5, len(decks_df.index) - min_index)):
                prompt += "\n " + str(i + 1) + ". " + decks_df.at[min_index + i, 'name'].replace(".csv", "")

        else:
            prompt = "\nOpen a Deck to edit: "
            prompt += "\n0. Go back 1 page."
            min_index = min(len(decks_df.index), min_index + tab_length)

            for i in range(min(5, len(decks_df.index) - min_index)):
                prompt += "\n " + str(i + 1) + ". " + decks_df.at[min_index + i, 'name'].replace(".csv", "")

        prompt += "\n6. Go forward 1 page."
        prompt += "\n7. Back"

        choice = get_int_range(prompt + "\nChoice: ", 0, tab_length + 2)

    deck_path = decks_df.at[min_index + choice - 1, 'name']

    return(deck_path)
