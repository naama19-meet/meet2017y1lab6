import turtle
UP_ARROW = 'Up'
LEFT_ARROW = 'Left'
DOWN_ERROW = 'Down'
RIGHT_ERROW = 'Righ'
SPACEBAR = 'space'

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

direction = UP

def up():
    global direction
    direction = UP
    print('you pressed up')
          
def down():
    global direction
    direction = DOWN
    print('you pressed down')

def left():
    global direction
    direction = LEFT
    print('you pressed left')
    
def right():
    global direction
    direction = RIGHT
    print('you pressed right')

#turtle.mainloop()
