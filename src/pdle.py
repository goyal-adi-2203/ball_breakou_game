# pdle.py to create and control movements of paddle 
# for the game


# turtle module to create the basic structure
from turtle import Turtle

# DIS to move for paddle in one movement
DIS = 70

# paddle class inheriting turtle class
class Paddle(Turtle):

    # function to define paddle properties
    def __init__(self):
        super().__init__()
        
        # creating paddle
        self.color('steel blue')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=10,stretch_wid=1)
        self.goto(x=0,y=-280)
    
    # left function moves paddle to the left
    def left(self):
        self.backward(DIS)
    
    # right function moves paddle to the left
    def right(self):
        self.forward(DIS)

    # function to reset
    def reset(self):
        self.goto(x=0,y=-280)