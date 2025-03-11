from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt", "r") as file:
            self.high_score =int(file.read())
        self.hideturtle()
        self.color("white")
        self.goto(0,250)
        self.refresh()





    def refresh(self):
        self.clear()
        self.write(f"Score : {self.score}, High Score : {self.high_score} ", align="center", font=("Arial", 20, "bold"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", "w") as file:
                file.write(str(self.score))

        self.score = 0
        self.refresh()

    def increase_score(self):
        self.score += 1
        self.refresh()


