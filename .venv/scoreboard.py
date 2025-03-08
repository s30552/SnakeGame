from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.goto(0,250)
        self.refresh()



    def refresh(self):
        self.clear()
        self.write(f"Score : {self.score} ", align="center", font=("Arial", 20, "bold"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER ", align="center", font=("Arial", 20, "bold"))