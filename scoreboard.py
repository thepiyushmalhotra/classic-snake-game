from turtle import Turtle
ALIGNEMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__() 
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.updateScore()
        

    def updateScore(self):
        self.write(f"Score: {self.score} ", align = ALIGNEMENT, font = FONT)

    def gameOver(self):
        self.goto(0,0)
        self.write("GAME OVER", align = ALIGNEMENT, font = FONT)

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.updateScore()

