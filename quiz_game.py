# Quiz Game

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["1) Mumbai", "2) New Delhi", "3) Kolkata", "4) Chennai"],
        "answer": 2,
    },
    {
        "question": "What is 5 + 7?",
        "options": ["1) 10", "2) 11", "3) 12", "4) 13"],
        "answer": 3,
    },
    {
        "question": "What color do you get when you mix red and white?",
        "options": ["1) Purple", "2) Pink", "3) Brown", "4) Orange"],
        "answer": 2,
    },
]

print("Welcome to the Quiz Game!")
print("Answer the questions by typing the number of the correct option.")
print()

score = 0

for item in questions:
    print(item["question"])
    for option in item["options"]:
        print(option)

    while True:
        answer = input("Your answer: ")
        if answer.isdigit() and 1 <= int(answer) <= len(item["options"]):
            break
        print("Please type the number of one of the options.")

    if int(answer) == item["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong answer.\n")

print(f"Quiz complete! You got {score} out of {len(questions)} correct.")
if score == len(questions):
    print("Excellent work! 🎉")
elif score >= 1:
    print("Good job! Keep learning.")
else:
    print("Keep practicing and try again.")
