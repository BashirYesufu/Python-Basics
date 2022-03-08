from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question['question'], question['correct_answer']))
print(question_bank[0].text)

quiz = QuizBrain(question_bank)
quiz.display_question()
