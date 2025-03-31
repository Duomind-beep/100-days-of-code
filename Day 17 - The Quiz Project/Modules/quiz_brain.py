class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_have_questions(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer,current_question.answer)
        if self.still_have_questions() is False:
            print("You completed the quiz!")
            print(f"Your final is {self.score}/{len(self.question_list)}")

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!!!")
            self.score += 1
        else:
            print("You got it wrong.")
        print(f"The correct answer was {correct_answer}.")
        print(f"The current score is {self.score}/{len(self.question_list)}")
        print("\n")





        # question_number += 1
        # self.q_text = q_text
        # choice = input("(True or False)")



# f"Q.{question_number+1}{question_bank[question_number]}(True/False)"