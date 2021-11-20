from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=('Courier', 15, 'normal'))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.ques_text = self.canvas.create_text(
            150, 125,
            text="Some Question Text",
            font=("Arial", 20, "italic"),
            width=280,
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_img, highlightthickness=0, command=self.right_pressed)
        self.right_button.grid(row=2, column=0)

        wrong_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_img, highlightthickness=0, command=self.wrong_pressed)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.ques_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.ques_text,
                text=f"You've reached the end of the quiz.\nYour final score is: {self.quiz.score}/{self.quiz.question_number}"
            )
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
