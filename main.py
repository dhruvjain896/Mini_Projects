import data
import question_model
from quiz_brain import QuizBrain

list_of_questions = []
for i in data.question_data:
    list_of_questions.append(question_model.Question(i["question"], i["correct_answer"]))

quiz = QuizBrain(list_of_questions)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")