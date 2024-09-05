from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Ariel", 14, 'bold')
SCORE_POSITIONS = [(50,240), (-80,240)]
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()  
        # keep track of the score of each player
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()      
    
    def update_scoreboard(self):
        self.clear()
        self.penup()
        self.goto(SCORE_POSITIONS[1])
        self.write(f"Score = {self.l_score}", align = ALIGNMENT, font = FONT)
        self.goto(SCORE_POSITIONS[0])
        self.write(f"Score = {self.r_score}", align = ALIGNMENT, font = FONT)
     
    def increase_l_score(self):
        self.l_score += 1
        self.update_scoreboard()
        
    def increase_r_score(self):
        self.r_score += 1
        self.update_scoreboard()