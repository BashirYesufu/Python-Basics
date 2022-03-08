class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        while not self.question_number == len(self.question_list):
            user_answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} "
                                f"(True/False): ").lower()
            if user_answer == self.question_list[self.question_number].answer.lower():
                self.score += 1
                print(f"Correct answer. Your score is {self.score}")
            else:
                print("wrong answer")
            self.question_number += 1
