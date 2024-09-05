from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Ariel", 14, 'bold')

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.setpos(-20,280)
        self.score = 0
        self.load_high_score()
        self.update_scoreboard()
                 
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score}, Highest_score = {self.highest_score}", align = ALIGNMENT, font = FONT)
     
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
    #def game_over(self):
    #    self.home()
    #    self.write("Game over.", align = ALIGNMENT, font = FONT)
        
    def update_highest_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("High_score.txt", mode="w") as file:
                file.write(f"{self.highest_score}")
        self.score = 0
        
    def load_high_score(self):
        with open("High_score.txt") as file:
            self.highest_score = int(file.read())
            
        