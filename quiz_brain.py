class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        curr_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {curr_question.text} (True/False)?: ")
        self.check_answer(answer, curr_question.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, question_answer):
        if answer.lower() == question_answer.lower():
            print("You got it right")
            self.score += 1
            print(f"Current score is: {self.score}/{self.question_number}")
            print("\n")
        else:
            print("Wrong, correct answer was", question_answer)
            print(f"Current score is: {self.score}/{self.question_number}")
            print("\n")

