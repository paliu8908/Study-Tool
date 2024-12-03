import AI
import Deck_Manipulator
import get_input
import multiple_choice
import open_question
import pandas as pd
import math
import AI_Quiz

import multiple_choice


def main():

    print("\nChoose: \n 1. New Deck \n 2. Edit Deck \n 3. Multiple Choice \n 4. Open Question \n 5. AI Quiz \n 6. Exit")
    option = get_input.get_int_range("Choice: ", 1, 5)

    while option != 6:
        if option == 1:
            Deck_Manipulator.create_deck()
        elif option == 2:
            edit_deck_menu()
        elif option == 3:
            multiple_choice_menu()
        elif option == 4:
            answer_question_menu()
        elif option == 5:
            ai_question_menu()

        print("\nChoose: \n 1. New Deck \n 2. Edit Deck \n 3. Multiple Choice \n 4. Open Question \n 5. AI Quiz \n 6. Exit")

        option = get_input.get_int_range("Choice: ", 1, 6)

def edit_deck_menu():
    deck_path = get_input.get_deck()

    print("\nChoose: \n1. Change Cards \n2. Delete Cards \n3. Add Cards \n4. AI Add \n5. Exit")

    option = get_input.get_int_range("Choice: ", 1, 4)

    while option != 5:
        if option == 1:
            Deck_Manipulator.edit_deck(deck_path)
        elif option == 2:
            Deck_Manipulator.delete_card(deck_path)
        elif option == 3:
            Deck_Manipulator.add_card(deck_path)
        elif option == 4:
            AI.ai_add(deck_path)

        print("\nChoose: \n1. Change Cards \n2. Delete Cards \n3. Add Cards \n4. AI Add \n5. Exit")

        option = get_input.get_int_range("Choice: ", 1, 5)

def multiple_choice_menu():
    deck_path = get_input.get_deck()

    q_num = get_input.get_int_range("How many questions?: ", 0, 100)

    multiple_choice.ask_questions(deck_path, q_num)

def answer_question_menu():
    deck_path = get_input.get_deck()

    q_num = get_input.get_int_range("How many questions?: ", 0, 100)

    open_question.quiz(deck_path, q_num)

def ai_question_menu():
    deck_path = get_input.get_deck()

    q_num = get_input.get_int_range("How many questions?: ", 0, 100)

    AI_Quiz.quiz(deck_path, q_num)

main()