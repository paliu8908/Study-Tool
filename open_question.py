import random
import pandas as pd
import get_input
import multiple_choice

def quiz(deck_path, q_num):
    correct = 0
    deck = pd.read_csv(deck_path)
    questions_available = len(deck.index)-1
    keywords = []
    response = ""
    ans_right = 0

    question_number = 0

    for i in range(q_num):
        ans_right = 0

        question = random.randint(0, questions_available)

        keywords = filter_keywords(multiple_choice.str_to_list(deck.loc[question, 'correct'], " "))

        response = filter_phrase(input("\n" + deck.loc[question, 'question'] + " "))

        for i in range(len(keywords) - 1):
            if not response.find(keywords[i].lower()) == -1:
                response.replace(keywords[i].lower(), "")
                ans_right += 1


        if ans_right/(i+1) > 0.75:
            print("\nCORRECT!")
            correct += 1
        else:
            print("\nWRONG. The correct answer was " + deck.loc[question, 'correct'])

    print("You got " + str(correct) +" questions correct. (" + format(correct/q_num, ".0%") + ")")

def filter_phrase(phrase):

    extraneous_words = ["a", "it", "are", "were", "the", "ing", "in", "of", "&"]

    for i in range(len(extraneous_words) - 1):
        phrase.replace(extraneous_words[i], "")

    return phrase.lower()

def filter_keywords(keywords):
    extraneous_words = ["a", "it", "are", "were", "the", "ing", "in", "of", "&"]

    for i in extraneous_words:
        if i in keywords:
            keywords.remove(i)

    return keywords