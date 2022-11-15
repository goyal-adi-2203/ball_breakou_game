# main.py for game background working

# turtle module for using console window
import turtle as t
import time

# importing classes 
# PADDLE 
from pdle import Paddle 
# UI
from ui import UI



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

# calling header function to write heading
ui.header()

# initialising game
game_pause = False
play_game = True


# function to end game
def end_game():
    global play_game
    play_game = False
    scr.bye()


# function to restart the game
def restart():
    global play_game
    pd.reset()
    # play_game = False
    time.sleep(0.5)
    # scr.bye()


scr.listen()

# defining which keys it needs to listen to, 
# which are the left and right arrow keys (to 
# move the paddle) and R to restart.
scr.onkey(key='Left',fun = pd.left)
scr.onkey(key='Right',fun = pd.right)
scr.onkey(key='r',fun = restart)
scr.onkey(key='s',fun = end_game)



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
