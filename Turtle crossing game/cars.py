from turtle import Turtle
import random

DISTANCE = 5

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(0.5,0.8)
        self.color(self.random_color())
        self.penup()
        self.setheading(180) 
        self.goto(380,random.randint(-250, 250))
        
    def random_color(self):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        return (r,g,b)
    
    def move(self):
        x = self.xcor()
        if x>-380:
            self.forward(DISTANCE)
        else:
            self.hideturtle()
            return 0
        
