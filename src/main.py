# main.py for game background working

# turtle module for using console window
import turtle as t
import time

# importing classes 
# PADDLE 
from pdle import Paddle 


# creating console background
scr = t.Screen()
scr.setup(width=1200,height=600)
scr.bgcolor('black')
scr.title('BREAKOUT')
scr.tracer(0)


# instances of classes
# PADDLE
pd=Paddle()

# initialising game
game_pause = False
play_game = True


# function to stop the game
def restart():
    global play_game
    play_game = False
    time.sleep(1)
    scr.bye()


scr.listen()

# defining which keys it needs to listen to, 
# which are the left and right arrow keys (to 
# move the paddle) and R to stop.
scr.onkey(key='Left',fun = pd.left)
scr.onkey(key='Right',fun = pd.right)
scr.onkey(key='r',fun = restart)


# starting the game
while play_game:

    time.sleep(0.02)    
    # playing if game not paused
    if not game_pause:
        # updating console
        scr.update()
        time.sleep(0.01)


t.mainloop()
