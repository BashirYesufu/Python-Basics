class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def display_question(self):
        while not self.question_number == len(self.question_list):
            user_answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} "
                                f"(True/False): ").lower()
            correct_answer = self.question_list[self.question_number].answer.lower()
            self.check_answer(user_answer, correct_answer)
        print(f"You've completed the quiz. Your total score is {self.score}/{len(self.question_list)}")

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print(f"Correct answer.\nYour score is {self.score}\n\n")
        else:
            print(f"wrong answer.\nYour score is {self.score}\n\n")
        self.question_number += 1
