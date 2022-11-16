# main.py for game background working

# turtle module for using console window
import turtle as t
import time

# importing classes 
# PADDLE 
from pdle import Paddle 
# UI
from ui import UI
# BRICKS
from bricks import Bricks
# scoreboard
from scrbrd import Scoreboard
# BALL 
from ball import Ball


# creating console background
scr = t.Screen()
scr.setup(width=1200,height=600)
scr.bgcolor('black')
scr.title('BREAKOUT')
scr.tracer(0)


# instances of classes
# PADDLE
pd=Paddle()
# UI
ui = UI()
# BRICKS
bricks = Bricks()
# scoreboard
score = Scoreboard(lives = 3)
# BALL
bl=Ball()



# calling header function to write heading
ui.header()

# initialising game
game_pause = False
play_game = True

# function to pause the game
def pause_game():
    global game_pause

    if game_pause:
        game_pause = False
    else:
        game_pause = True
    
    
# function to end game
def end_game():
    global play_game
    play_game = False
    scr.bye()

# function to restart the game
def restart():
    global game_pause,play_game,bl,score,pd,bricks
    game_pause = False 
    play_game = True
    bl.reset()
    score.reset()
    bricks.reset()
    pd.reset()
    time.sleep(0.5)


scr.listen()

# defining which keys it needs to listen to, 
# which are the left and right arrow keys (to 
# move the paddle) s to stop and R to restart.
scr.onkey(key='Left',fun = pd.left)
scr.onkey(key='Right',fun = pd.right)
scr.onkey(key='r',fun = restart)
scr.onkey(key='s',fun = end_game)
scr.onkey(key='space',fun = pause_game)



# CHECKING THE COLLISIONS OF BALL 
# collision with WALLS
def check_coll_walls():

    global bl,score,play_game,ui

    # collision with left and right walls
    if bl.xcor() < -580 or bl.xcor() > 570:
        bl.bounce(x_bounce=True,y_bounce=False)
        return

    # collision with upper wall
    if bl.ycor() > 270 :
        bl.bounce(x_bounce=False,y_bounce=True)
        return

    # collision with lower wall, 
    # in which case user fails and game resets
    if bl.ycor() < -280:
        bl.reset()
        score.dec_lvs()

        # GAME OVER and uses lost if lives = 0
        if score.lvs == 0:
            score.reset()
            play_game = False
            ui.GO(W=False)
            return
        return


# starting the game
while play_game:

    time.sleep(0.02)    
    # playing if game not paused
    if not game_pause:
        # updating console
        scr.update()
        time.sleep(0.01)
    
scr.bye()
t.mainloop()
