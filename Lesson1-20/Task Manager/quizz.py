import json

with open("files/questions.json", "r") as file:
    content = file.read()

#converts a string to a list
data = json.loads(content)
score = 0

for question in data:
    print(question["question"])
    for index, answer in enumerate(question["answers"]):
        print(index + 1, "-", answer)
    user_answer = int(input("What's your answer?"))
    question["user_choice"] = user_answer

for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score+= 1
        result = "CORRECT!!!"
    else:
        result = "Wrong..."
    message = f"Question {index + 1}: Your answer was {question["user_choice"]}, the correct answer is: {question["correct_answer"]} -> {result}"
    print(message)
print("Score:", score, "/", len(data))