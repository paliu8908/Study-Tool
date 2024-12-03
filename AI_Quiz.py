import google.generativeai as genai
import pandas as pd
import random

def quiz(deck_path, q_num):
    genai.configure(api_key="AIzaSyCnzgHUAL-LoKXioMs-TT_q5bzdCvxUK5Q")

    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    correct = 0
    deck = pd.read_csv(deck_path)
    questions_available = len(deck.index)-1
    solution = []
    response = ""
    ans_right = 0

    question_number = 0

    for i in range(q_num):
        ans_right = 0



        question = random.randint(0, questions_available)

        solution = deck.loc[question, 'correct']

        response = input("\n" + deck.loc[question, 'question'] + " ")

        ans_right = model.generate_content("what % are these two sentences similar?" + solution.lower() + "\n"
                    + response.lower() + "generate response as 1 number").text

        try:
            ans_right = int(ans_right)
        except ValueError:
            ans_right = 0

        if ans_right >= 75:
            print("\nCORRECT! Score of " + str(ans_right))
            correct += 1
        elif solution.lower() == response.lower():
            print("\nCORRECT!")
            correct += 1
        else:
            print("\nWRONG.  Score of " + str(ans_right) + "\nThe correct answer was " + deck.loc[question, 'correct'])

    print("You got " + str(correct) +" questions correct. (" + format(correct/q_num, ".0%") + ")")