from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align='center', font=('Arial', 13, 'normal'))

    def game_over(self):
        self.color("white")
        self.goto(0, 0)
        self.write("Game Over !", align='center', font=('Times New Roman', 20, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
