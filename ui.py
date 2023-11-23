from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, pady=10)

        self.canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=285,
                                                     text="Some Question Text",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 18, "italic"))
        self.canvas.grid(column=0,
                         row=1,
                         columnspan=2,
                         padx=20,
                         pady=20)

        self.score_label = Label(text="Score: 0",
                                 font=("Arial", 14),
                                 foreground="white",
                                 background=THEME_COLOR)

        self.score_label.grid(column=1,
                              row=0,
                              padx=20,
                              sticky=E)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=lambda: self.check_answer("true"))
        self.true_button.grid(column=0, row=2, pady=20)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=lambda: self.check_answer("false"))
        self.false_button.grid(column=1, row=2, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.true_button.config(state="active")
            self.false_button.config(state="active")
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of quiz. "
                                                            f"Your final score is {self.quiz.score}.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_answer(self, user_answer):
        if self.quiz.check_answer(user_answer):
            self.give_feedback(True)
        else:
            self.give_feedback(False)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")

        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.window.after(1000, self.get_next_question)
