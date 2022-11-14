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



scr.listen()

# defining which keys it needs to listen to, 
# which are the left and right arrow keys (to 
# move the paddle) 
scr.onkey(key='Left',fun=pd.left)
scr.onkey(key='Right',fun=pd.right)


scr.update()

t.mainloop()
