# bricks.py to create and control appearance and 
# disappearance of bricks in the game


# turtle module to create the basic structure
from turtle import Turtle

# class Brick for one brick definition
# Brick class inheriting Turtle class
class Brick(Turtle):

    # function to define brick's properties
    def __init__(self,x_cor,y_cor):
        super().__init__()
        self.penup()

        # creating brick
        self.shape('square')
        self.shapesize(stretch_len=3,stretch_wid=1.5)
        
        # assigning them color
        self.color('red')
        self.goto(x=x_cor,y=y_cor)

        # border
        self.left_wall = self.xcor() - 30 
        self.right_wall = self.xcor() + 30 
        self.upper_wall = self.ycor() + 15 
        self.bottom_wall = self.ycor() - 15 

# class Bricks for definition of collection of bricks
class Bricks:

    # function for the properties of collection
    def __init__(self) -> None:
        self.y_str = 0
        self.y_end = 240
        self.brks = []
        self.crt_lanes()

    # function for one lane of bricks
    def crt_lane(self,y_cor):
        for i in range(-570,570,63):
            brick = Brick(i,y_cor)
            self.brks.append(brick)
    
    # function for all the lanes
    def crt_lanes(self):
        for i in range(self.y_str,self.y_end,32):
            self.crt_lane(i)
    
    # funciton to reset
    def reset(self):
        self.y_str = 0
        self.y_end = 240
        self.brks = []
        self.crt_lanes()
