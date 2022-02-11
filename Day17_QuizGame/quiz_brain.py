class QuizBrain:

    def __init__(self, q_list):
        # keep track of which question user is on
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # TODO: checking if we're at the end of the quiz
    def still_has_questions(self):
        """Returns boolean. Depending on boolean, while loops continues or while loop stops once quiz has questions."""
        # if self.question_number < len(self.question_list):
        #     print(self.question_number)
        #     return True
        # else:
        #     return False
        # can make this way simpler and just return
        return self.question_number < len(self.question_list)

    # TODO: asking the questions

    def next_question(self):
        # retrieve item at current question_number from question_list
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        # use input() function to show Question text and user's answer
        # because each object in question_bank = question object -> has text and answer attributes
        user_answer = input(f"Q.{self.question_number}: {current_q.text} (True/False?) ")
        self.check_answer(user_answer, current_q.answer)

    # TODO: checking if the answer was correct
    def check_answer(self, user_answer, correct_answer):
        # drop both sides to lower case to compare
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You fot it right!")
        else:
            print("That's wrong")
        print(f"The correct is {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")


