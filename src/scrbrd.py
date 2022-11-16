# scrbrd.py to keep track of scores via 
# a text file of the game  

# turtle module to create
from turtle import Turtle

# file containing high score
FILE = 'C:/Users/91826/projects/Games and projects/ball_breakout_game/HighScore.txt'

# checking for the high score in text file 
# if score not found either creating file or 
# not high score = 0
try:
    score = int(open(FILE,'r').read())
except FileNotFoundError:
    score = open(FILE,'w').write(str(0))
except ValueError:
    score = 0

FONT = ('calibri',18,'normal')

# class Scoreboard for scoreboard defintions
# inheriting Turtle class
class Scoreboard(Turtle):

    # functon for scoreboard properties
    def __init__(self, lives) -> None:
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()

        # writing high score
        self.hs = score
        self.goto(x=-580,y=260)

        self.lvs=lives
        self.score = 0

        # updating score
        self.update_scr()
    
    # function to update score
    def update_scr(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score : {self.hs} | Lives : {self.lvs}" , align = 'left' ,font = FONT )
        
    # increasing score
    def inc_score(self):
        self.score += 1
        
        # if greater than high score then updating 
        # high score
        if self.score > self.hs : 
            self.hs += 1
        self.update_scr()

    # decreasing lives
    def dec_lvs(self):
        self.lvs -= 1
        self.update_scr()

    # when game ends resetting scores
    def reset(self) -> None:
        self.clear()
        self.score = 0
        self.update_scr()
        open(FILE,'w').write(str(self.hs))
