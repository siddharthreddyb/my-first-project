questions = [
    {
        "QAS": "what is the capital of AndhraPradesh?",
        "option": ["A. Amaravathi", "B. Vishakapatnam", "C. None of the above"],
        "ANS": "C"
    },
    {
        "QAS": "what is the capital of Karnataka?",
        "option": ["A. Bengaluru", "B. Mysour", "C. None of the above"],
        "ANS": "A"
    },
    {
        "QAS": "what is the capital of Tamil nadu?",
        "option": ["A. Kanchipuram", "B. Chennai", "C. None of the above"],
        "ANS": "B"
    },
    {
        "QAS": "what is the capital of Telangana?",
        "option": ["A. Amaravathi", "B. Vishakapatnam", "C. Hyderabad"],
        "ANS": "C"
    }
]
def run_quiz(questions):
    score = 0
    for Question in questions:
        print(Question["QAS"])
        for option in Question["option"]:
            print(option)
        ANS = input("Enter your answer(A, B, or C): ")
        if ANS == Question["ANS"]:
            print("correct\n")
            score += 1
        else:
            print("wrong\n")
        print(f"You got {score} out of {len(questions)} questions correct.")
run_quiz(questions)
            
