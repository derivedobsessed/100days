from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quizzer = QuizBrain(question_bank)
game_on = True
while quizzer.still_has_questions() and game_on:
    game_on = quizzer.answer_correct()
