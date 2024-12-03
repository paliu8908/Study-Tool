import pandas as pd

import get_input
from get_input import get_int_range


def create_deck() :

    deck_list_path = 'files.csv'

    questions_df = {'question' : [],
                    'correct' : [],
                    'false' : []}

    questions_df = pd.DataFrame(questions_df)

    #Vars

    if_create = False
    ans = ""
    deck_name = ""


    decks_df = pd.read_csv(deck_list_path)

    #print(decks_df.head())

    if_create = get_input.get_bool("Would you like to create a deck?")

    if if_create:
        deck_name = input("What is the deck name?")

        deck_name += ".csv"

        deck = open(deck_name, "x")
        questions_df.to_csv(deck_name, index=False)

        decks_df.loc[len(decks_df.index) + 1, 'name'] = deck_name
        decks_df.to_csv('files.csv', index=False)

def edit_deck(deck_path):

    deck_info = pd.read_csv(deck_path)

def delete_card(deck_path):

    deck_info = pd.read_csv(deck_path)

def add_card(deck_path):
    otherOptions = 0
    wrong = []

    cards_df = pd.read_csv(deck_path)

    question = input("Question: ")
    answer = input("Correct Response: ")

    otherOptions = get_int_range("Number of Other Answers: ", 0, 10)

    for i in range(otherOptions):
        wrong.append(input("Other Responses: "))

    #print([question, answer, wrong])
    cards_df.loc[len(cards_df.index)] = [question, answer, wrong]

    cards_df.to_csv(deck_path, index=False)

