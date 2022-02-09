class QuizBrain:

    def __init__(self, q_list):
        # keep track of which question user is on
        self.question_number = 0
        self.question_list = q_list

    # TODO: asking the questions
    # retrieve item at current question_number from question_list
    # use input() function to show Question text and user's answer
    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        # because each object in question_bank = question object -> has text and answer attributes
        input(f"Q.{self.question_number}: {current_q.text} (True/False?) ")


# TODO: checking if the answer was correct
# TODO: checking if we're at the end of the quiz