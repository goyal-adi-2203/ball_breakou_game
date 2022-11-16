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

TEMP = False

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
    global game_pause,ui
    if game_pause:
        # ui.header()
        game_pause = False
    else:
        game_pause = True
    
    
# function to end game
def stop():
    global play_game
    play_game = False


scr.listen()

# defining which keys it needs to listen to, 
# which are the left and right arrow keys (to 
# move the paddle) s to stop and R to restart.
scr.onkey(key='Left',fun = pd.left)
scr.onkey(key='Right',fun = pd.right)
scr.onkey(key='s',fun = stop)
scr.onkey(key='space',fun = pause_game)



# CHECKING THE COLLISIONS OF BALL 

# WALLS
def check_coll_walls():

    global bl,score,play_game,ui

    # collision with left and right walls
    if bl.xcor() < -580 or bl.xcor() > 570:
        bl.bounce(x_bounce=True,y_bounce=False)
        return

    # collision with upper wall
    if bl.ycor() > 240 :
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
            ui.GO(W=False)
            time.sleep(2)
            play_game = False
            return
        return


# PADDLE
def check_coll_paddle():
    
    global bl,pd

    # x coordinates of paddle and ball
    pd_x = pd.xcor()
    bl_x = bl.xcor()

    # checking for coll
    # by using centre of ball and paddle
    if bl.distance(pd) < 110 and bl.ycor() < -250 :
        
        # when paddle is right of scr
        if pd_x > 0:
            if bl_x > pd_x:
                # balls hits left side
                bl.bounce(x_bounce=True,y_bounce=True)
                return
            
            else:
                bl.bounce(x_bounce=False,y_bounce=True)
                return
        
        # when paddle is left of scr
        elif pd_x < 0 :
            if bl_x < pd_x:
                # balls hits left side
                bl.bounce(x_bounce=True,y_bounce=True)
                return
            
            else:
                bl.bounce(x_bounce=False,y_bounce=True)
                return
        
        # paddle in centre
        else:
            if bl_x == pd_x:
                bl.bounce(x_bounce=False,y_bounce=True)
                return
            else:
                bl.bounce(x_bounce=True,y_bounce=True)
                return

# BRICKS
def check_coll_brick():

    global bl,bricks,score


    for brick in bricks.brks:

        # when ball in range
        if bl.distance(brick) < 40: 
            
            brick.clear()
            brick.goto(3000,3000)
            bricks.brks.remove(brick)
            
            # detection coll to bounce the ball
            # LEFT 
            if bl.xcor() < brick.left_wall:
                bl.bounce(x_bounce=True,y_bounce=False)
                
            # RIGHT
            elif bl.xcor() > brick.right_wall:
                bl.bounce(x_bounce=True,y_bounce=False)
            
            # BOTTOM 
            elif bl.ycor() < brick.bottom_wall:
                bl.bounce(x_bounce=False,y_bounce=True)
            
            # TOP
            elif bl.ycor() > brick.upper_wall:
                bl.bounce(x_bounce=False,y_bounce=True)

            # increasing score
            score.inc_score()


time.sleep(1)
# starting the game
while play_game:

    # playing if game not paused
    if not game_pause:
        
        if TEMP:
            TEMP = False
            ui.header()

        # updating console
        scr.update()
        time.sleep(0.02)      
        bl.move()

        # checking collisions with walls
        check_coll_walls()

        # checking collision with paddle
        check_coll_paddle()
    
        # checking collisions with bricks
        check_coll_brick()
        
        # checking for win situation
        if len(bricks.brks) == 0:
            ui.GO(W=True)
            break
    
    else:
        TEMP = True
        ui.when_pause(score.score)
    

scr.bye()
t.mainloop()
