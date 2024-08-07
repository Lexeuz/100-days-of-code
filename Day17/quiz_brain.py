class QuizBrain:

    def __init__(self, q_list):
        self.question_list = q_list
        self.question_n = 0
        self.score = 0

    def still_has_question(self):
        return self.question_n < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_n]
        self.question_n += 1
        user_answer = input(
            f"Q.{self.question_n}: {current_question.text} (True/False): "
        )
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, u_answer, c_answer):
        if u_answer.lower() == c_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That is wrong!")
        print(f"The correct answer was: {c_answer}")
        print(f"Your current score is: {self.score}/{self.question_n}\n")
