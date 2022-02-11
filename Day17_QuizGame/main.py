from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# create question bank that contains list of question objects each initialized with question and answer
question_bank = []
# loop through question data
for question in question_data:
    # create Question object from each entry in question data
    question_object = Question(question["question"], question["correct_answer"])
    # append each Question object to question bank
    question_bank.append(question_object)

# we're converting data which has str key (easy to make typos) and convert it object
# -> easier and foolproof way to access

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions(): # if quiz still has questions remaining
    quiz.next_question()

print("You completed the quiz.")
print(f"Your score is {quiz.score}/{quiz.question_number}.")



