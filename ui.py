import tkinter
from quiz_brain import QuizBrain  # <--- learned something ...

THEME_COLOR = "#375362"


class QuizInterface:
    """
    ...
    """

    # class (instance) attributes

    def __init__(self, quiz_brain: QuizBrain):  # <--- ... new; an object instance
                                                # passed as an argument (when
                                                # instantiating the QuizInterface
                                                # class) must be of type QuizBrain
        # accessing QuizBrain class object instance via
        # the concept of composition
        self.quiz = quiz_brain

        # window
        self.window = tkinter.Tk()
        self.window.title(string='Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # label
        self.score_label = tkinter.Label(text='Score: 0', bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1)
        # self.score_label.grid(row=0, column=1, pady=(0, 50))
        # self.score_label.grid(row=0, column=1, pady=(0, 40))

        # canvas
        self.canvas = tkinter.Canvas(bg='white', width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="< Question goes here >",
            font=("Arial", 20, "italic"), fill=THEME_COLOR)
        # self.get_next_question()
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # button(s)
        true_btn_img = tkinter.PhotoImage(file="./images/true.png")
        self.true_button = tkinter.Button(
            image=true_btn_img,
            highlightthickness=0,
            # command=self.quiz.check_answer('True')
            command=self.user_chose_true
        )
        self.true_button.grid(row=2, column=0)
        # self.true_button.grid(row=2, column=0, pady=(50, 0))
        false_btn_img = tkinter.PhotoImage(file="./images/false.png")
        self.false_button = tkinter.Button(
            image=false_btn_img,
            highlightthickness=0,
            # command=self.quiz.check_answer('False')
            command=self.user_chose_false
        )
        self.false_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label['text'] = 'Score: {user_score}'.format(user_score=self.quiz.score)
            # self.canvas.config(bg='white')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(tagOrId=self.question_text, text=q_text)
        else:
            self.true_button.config(state='disabled')  # <--- learned something new; canvas.itemconfig
                                                       # does not have to always be used when changing
                                                       # canvas widgets' properties
            self.false_button.config(state='disabled')
            self.canvas.itemconfig(tagOrId=self.question_text, text='You\'ve reached the end of '
                                                                    'the quiz! How\'d you do?')

    def user_chose_true(self):
        self.give_user_feedback(self.quiz.check_answer('True'))

    def user_chose_false(self):
        self.give_user_feedback(self.quiz.check_answer('False'))

    def give_user_feedback(self, is_user_right):
        if is_user_right:
            # self.canvas.itemconfig(tagOrId=self.canvas, bg='green')  # canvas is not a canvas item
                                                                       # - it's the canvas itself!
            self.canvas.config(bg='green')
        else:
            # self.canvas.itemconfig(tagOrId=self.canvas, bg='red')
            self.canvas.config(bg='red')
        self.window.after(ms=1000, func=self.get_next_question)
