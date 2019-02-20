from Question import Question

test = [
    "What color is a banana?\n  a. white\n  b. blue\n  c. yellow",
    "What color is a strawberry?\n  a. white\n  b. red\n  c. yellow",
    "Who is the president of SA\n  a. mugabe\n  b. ramaposa\n  c. radebe"
]

ques = [
    Question(test[0], 'c'),
    Question(test[1], 'b'),
    Question(test[2], 'b')
]

def run(questions):
    score = 0
    for i in questions:
        print(i.prompt+"\n")
        answer = input("Answer: ")
        if answer == i.answer:
            score += 1
    if score == 3:
        print(f"\n!!!Wow what an exciting peformance {score}/{len(questions)}!!!!")
    else:
        print(f"You scored {score}/{len(questions)}")

run(ques)
input()
