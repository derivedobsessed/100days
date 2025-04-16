class QuizBrain:

    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        return input(f'Q{self.question_number}. {question.text} (True/False): ')

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def answer_correct(self):
        question = self.question_list[self.question_number]
        if self.next_question() == question.answer:
            print('You got it right!')
            self.score += 1
            return True
        else:
            print(f'Wrong! The answer is {question.answer}. You answered {self.score} questions correctly.')
            return False
