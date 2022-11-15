# ui.py to write methods required for user 
# interface of the game

# importing turtle class from turtle module
from turtle import Turtle
import time,random

FONT = ('calibri',52,'normal')
FONT2 = ('calibri',14,'normal')
ALIGN = 'center'


# class UI inheriting Turtle
class UI(Turtle):

    # function for turtle properties to write
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('blue')
        self.header()

    # function for the heading
    def header(self):
        self.clear()
        self.goto(x = 0,y=-150 )
        self.write('BREAKOUT',align=ALIGN,font=FONT)
        self.goto(x=0,y=-180)
        self.write('Press Space to PAUSE or RESUME the Game',
            align=ALIGN,font=FONT2)

    # function to show win/lose after the game ends
    def GO(self,W):
        self.clear()
        if W == True:
            self.write("You Cleared the Game", align=ALIGN,font=FONT)
        else:
            self.write("Game Over! :( ",align=ALIGN,font=FONT)
    
