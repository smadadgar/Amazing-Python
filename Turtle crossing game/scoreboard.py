from turtle import Turtle
ALIGNMENT = 'center'
FONT=("Ariel", 14, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-350, 260)
        self.write(f"Level: {self.level}", align = ALIGNMENT, font = FONT)
        
    def level_up(self):
        self.level += 1
        self.update_scoreboard()
        
    def game_over(self):
        self.home()
        self.write("Game over.", align = ALIGNMENT, font = FONT)