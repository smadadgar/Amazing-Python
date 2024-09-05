from turtle import Turtle, Screen
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVING_DISTANCE = 20

class Snake:
    
    def __init__(self, width, height):
        self.segments = []
        self.width = width
        self.height = height
        self.create_screen()
        self.create_snake()
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            
    def reset(self): # reset the snake
        for seg in self.segments:
            seg.goto(-1000,1000) # this is somewhere outside the game window
        # create a new segment
        self.segments.clear()
        self.create_snake()
        
    def create_screen(self):
        self.screen = Screen()
        self.screen.setup(width = self.width, height = self.height)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.tracer(0)
          
    def add_segment(self,position):
        new_segment = Turtle(shape = "square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
       
    def extend(self):
        self.add_segment(self.segments[-1].position())
        
    def position(self):
        self.poses = []
        for seg in self.segments:
            self.poses.append(seg.pos())
      
    def go_right(self):
        if self.segments[0].heading() != 180: # avoid backward move
            self.segments[0].setheading(0)
            self.segments[0].forward(MOVING_DISTANCE)
            for i in range(1,len(self.segments)):
                self.segments[i].goto(self.poses[i-1])

    def go_left(self):
        if self.segments[0].heading() != 0: # avoid backward move
            self.segments[0].setheading(180)
            self.segments[0].forward(MOVING_DISTANCE)
            for i in range(1,len(self.segments)):
                self.segments[i].goto(self.poses[i-1])
            
    def go_up(self):
        if self.segments[0].heading() != 270: # avoid backward move
            self.segments[0].setheading(90)
            self.segments[0].forward(MOVING_DISTANCE)
            for i in range(1,len(self.segments)):
                self.segments[i].goto(self.poses[i-1])
            
    def go_down(self):
        if self.segments[0].heading() != 90: # avoid backward move
            self.segments[0].setheading(270)
            self.segments[0].forward(MOVING_DISTANCE)
            for i in range(1,len(self.segments)):
                self.segments[i].goto(self.poses[i-1])
            
    def move(self):        
        self.screen.listen()
        self.position()
        self.screen.onkey(self.go_right, 'Right')
        self.screen.onkey(self.go_left, 'Left')
        self.screen.onkey(self.go_up, 'Up')
        self.screen.onkey(self.go_down, 'Down')
        
        