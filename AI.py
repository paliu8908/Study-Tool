import google.generativeai as genai
import pandas as pd
import get_input

def ai_add(deck_path):
    genai.configure(api_key="AIzaSyCnzgHUAL-LoKXioMs-TT_q5bzdCvxUK5Q")

    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    otherOptions = 0
    wrong = []

    cards_df = pd.read_csv(deck_path)

    question = input("Question: ")
    answer = input("Correct Response: ")

    wrong_ans = model.generate_content("Generate a multiple choice question on " +
                                       question + "with the solution " + answer + "Generate only the answers and no solution.").text

    wrong = wrong_ans.splitlines()
    new_wrong = []

    ans_str = answer.replace(",", "").replace(".", "").lower()

    for i in wrong:
        cut_str = i.lower().replace("," , "").replace(".", "")
        if cut_str.find(ans_str) < 0 and i.find(answer) < 0 < len(i) and i.find("Correct") < 0:
            new_wrong.append(i[3:].replace(",", "").replace("\"", "").lstrip())

    cards_df.loc[len(cards_df.index)] = [question, answer, new_wrong]

    cards_df.to_csv(deck_path, index=False)

