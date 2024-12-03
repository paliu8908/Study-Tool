import random

import pandas as pd

import get_input


def ask_questions(deck_path, q_num):
    correct = 0
    deck = pd.read_csv(deck_path)
    questions_available = len(deck.index)-1
    ans_options = []
    question_number = 0
    ans = ""

    for i in range(q_num):
        question = random.randint(0, questions_available)
        correct_location = -1

        print("\n" + deck.loc[question, 'question'])

        ans_options = str_to_list(deck.loc[question, 'false'], ",")
        ans_options.append(" " + deck.loc[question, 'correct'])



        for j in range(len(ans_options)):
            question_number = random.randint(0, len(ans_options)-1)

            if question_number == len(ans_options) - 1 and correct_location == -1:

                correct_location = j+1

            print(" " + str(j+1) + ". " + ans_options[question_number])

            ans_options.pop(question_number)

        ans = get_input.get_int_range("Answer: ", 1, j+1)

        if ans == correct_location:
            print("\nCORRECT!")

            correct += 1
        else:
            print("\nWRONG. The correct answer was " + str(correct_location))

    print("You got " + str(correct) +" questions correct. (" + format(correct/q_num, ".0%") + ")")

def str_to_list(str, deliminter):
    str = " " + str
    str = str.replace("[", "")
    str = str.replace("]", "")
    str = str.replace("'", "")

    return list(str.split(deliminter))