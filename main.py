from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question = Question(i["text"], i["answer"])
    question_bank.append(question)
quizbrain = QuizBrain(question_bank)

while quizbrain.still_has_question():
    quizbrain.next_question()
print("You have completed the quiz")
print(f"Your final score was: {quizbrain.score}/{quizbrain.question_number}")