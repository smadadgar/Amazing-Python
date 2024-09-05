from turtle import Turtle
import random

DISTANCE = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.8,0.8)
        self.color("white")
        self.penup()
        self.x_move = random.choice([-1,1]) * DISTANCE
        self.y_move = DISTANCE
        self.move_speed = 0.1
        
    def go_origin(self):
        self.home()
        self.x_move *= -1 # or self.bounce("x")
        self.y_move = DISTANCE
        self.move_speed = 0.1
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
    def bounce(self, change_dir):
        if change_dir == "x":
            self.x_move *= -1 # this changes the x direction (this happens when a ball hits a paddle)
            self.move_speed *= 0.9 # this increases the speed each time it hits a paddle
        if change_dir == "y":
            self.y_move *= -1 # this changes the y direction (this happens when a ball hits a up or down wall)
        
       
     

