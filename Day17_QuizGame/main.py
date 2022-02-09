from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# create question bank that contains list of question objects each initialized with question and answer
question_bank = []
# loop through question data
for question in question_data:
    # create Question object from each entry in question data
    question_object = Question(question["text"], question["answer"])
    # append each Question object to question bank
    question_bank.append(question_object)

# we're converting data which has str key (easy to make typos) and convert it object
# -> easier and foolproof way to access

q = QuizBrain(question_bank)
q.next_question()




