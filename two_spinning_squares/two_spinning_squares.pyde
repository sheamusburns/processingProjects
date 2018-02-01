w = 0
h = 0
angle = 0
velocityX = 1
velocityY = 1

def setup():
    global w, h
    size(500, 500)
    rectMode(RADIUS)
    h = height/3
    w = width/3
    angle = 1

def draw():
    global angle, w, h, velocityX, velocityY
    background(30, 30, 0)
    translate(width/2, height/2)
    rotate(radians(angle))
    fill(255, 255, 255)
    rect(0, 0, w, h)
    rotate(radians(-2*angle))
    fill(0, 0, 0)
    rect(0,0,w/2,h/2)
    angle += 1
    
    #How can you change this code so the user can control the rate of change.
    if w >= width/2:
        velocityX = -1
    elif w <= 0:
        velocityX = 1
    w+= velocityX
    if h >= height/2:
        velocityY = -1
    elif h <= 0:
        velocityY = 1
    h += velocityY
    
    #can you use a for loop to generate a grid of diamonds - 4 diamonds in width and 4 in height?
        
    