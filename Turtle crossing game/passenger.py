from turtle import Turtle
DISTANCE = 10

class Passenger(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(0,-280)
        self.control_speed = 1
        
    def move(self):
        self.forward(DISTANCE)
        
    def cross_again(self):
        self.goto(0,-280)
        self.control_speed *= 0.8