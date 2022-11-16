# ball.py to create and control movements of ball 
# for the game


# turtle module to create the basic structure
from turtle import Turtle

# DIS to move for ball in one movement
DIS = 10

# Ball class inheriting turtle class
class Ball(Turtle):

    # left function moves paddle to the left
    def left(self):
        self.backward(DIS)
    
    # right function moves paddle to the left
    def right(self):
        self.forward(DIS)

    # function to define ball's properties
    def __init__(self):
        super().__init__()

        # creating ball
        self.color('white')
        self.shape('circle')
        self.penup()

        # movement of ball each time
        self.x_move_dist=DIS
        self.y_move_dist=DIS
    
    # function to update the coordinates of ball
    def move(self):
        
        # moving 10 units in horizontal and 
        # vertical directions
        new_y=self.ycor() + self.y_move_dist
        new_x=self.xcor() + self.x_move_dist
        self.goto(x=new_x,y=new_y)
    
    # function to bounce the ball in case of collision
    def bounce(self,x_bounce,y_bounce):

        # reversing direction horizontally
        if x_bounce:
            self.x_move_dist*=-1

        # reversing direction vertically
        if y_bounce:
            self.y_move_dist*=-1
    
    # function to reset the ball's position in case 
    # of losing a life
    def reset(self):
        self.goto(x=0,y=-240)
        self.y_move_dist = DIS
        self.x_move_dist = DIS
