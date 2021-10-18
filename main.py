# NOTE: the principles of oop (object-oriented programming) are maintained where
#       each module is responsible for its own thing; the QuizBrain is responsible
#       for managing the quiz, getting questions and keeping track of score whereas
#       the QuizInterface is responsible for putting those things onto the screen
#       to be displayed

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)  # in relation to the new thing learned,
                               # this also ensures no mistakes are
                               # made when the QuizInterface (class)
                               # is initialized
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
