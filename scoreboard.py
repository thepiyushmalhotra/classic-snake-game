from turtle import Turtle
ALIGNEMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__() 
        self.score = 0
        with open("E:\Coding World !!\Angela Yu Python\Python Practice\Snake Game\data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.updateScore()
        

    def updateScore(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score} ", align = ALIGNEMENT, font = FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("E:\Coding World !!\Angela Yu Python\Python Practice\Snake Game\data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.updateScore()

    def increaseScore(self):
        self.score += 1
        self.updateScore()

