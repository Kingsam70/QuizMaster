from tkinter import *
from quizbrain import QuizBrain

THEME_COLOR = "skyblue"


class Gui:
    def __init__(self, quiz_data: QuizBrain):
        self.score = 0

        self.quiz_brain = quiz_data

        self.window = Tk()
        self.window.title("Quizz")
        self.window.config(padx=20, pady=60, bg=THEME_COLOR)
        self.score_label = Label(text=f"Score: {self.score}", font=12, bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=400, height=300)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30)
        self.canvas_text = self.quiz_brain.question_text

        self.text = self.canvas.create_text(200, 150, text=self.canvas_text, font=8, width=380)

        right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_image, highlightthickness=0, command=self.right_command)
        # self.right_button.photo = right_image
        self.right_button.grid(column=1, row=2)

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.wrong_command)
        # self.wrong_button.photo = wrong_image
        self.wrong_button.grid(column=0, row=2)

        self.window.mainloop()

    def next_question_bg_change(self):
        """checks if the game is over and if not gives the next question and changes bg of canvas back to white"""
        if self.quiz_brain.question_no == self.quiz_brain.length_data - 1:
            self.canvas.itemconfig(self.text, text="GAME OVER")

            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
            print("Disabled")

        else:
            self.quiz_brain.next_question()
            self.canvas.itemconfig(self.text, text=self.quiz_brain.question_text)

        self.canvas.config(bg="white")

    def right_command(self):
        """executes when right_button is clicked"""
        return_value = self.quiz_brain.check_answer("True")
        if return_value:
            self.canvas.config(bg="green")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.next_question_bg_change)

    def wrong_command(self):
        """executes when left_button is clicked"""
        return_value = self.quiz_brain.check_answer("False")
        if return_value:
            self.canvas.config(bg="green")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.next_question_bg_change)
