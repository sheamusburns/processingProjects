from wall import Wall
from ball import Ball
    
def setup():
    global b1, wall
    size(500, 500)
    # b1 = Ball(20, width/2, height/2, (255, 255, 0))
    wall = Wall(60, 10, width/2, height-50, 0, 0, 3)
    
def draw():
    # print(keyCode)
    global b1, wall
    background(255, 255, 255)
    # b1.changeX(2)
    # b1.changeY(.5)
    # b1.render()
    wall.render()
    
def keyPressed():
    global wall
    wall.arrow()
    