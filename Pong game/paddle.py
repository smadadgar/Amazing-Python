from turtle import Turtle

DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.create_paddle()
        
    def create_paddle(self):
        self.shape("square")
        self.shapesize(stretch_wid = 1, stretch_len = 3)
        self.color("white")
        self.penup()
        self.setheading(90)
        self.goto(self.position)
            
    def up(self):
        self.setheading(90)
        self.forward(DISTANCE)
        
    def down(self):
        self.setheading(270)
        self.forward(DISTANCE)
        
    def move(self):
        self.forward(DISTANCE)
        
        


        
       