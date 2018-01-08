x=width/2
y=height/2
changeX = 0
changeY = 0
radius = 30

def setup():
    global x, y
    size(500, 500)
    x = width/2
    y = height/2
    ellipse(x, y, 2*radius, 2*radius)
    frameRate(40)
    
def draw():
    global x, y, changeX, changeY
    background(20)
    x += changeX
    y += changeY
    
    #check if ball hits the edge and reverse vector
    if x > width - radius or x < 0 + radius:
        changeX = -changeX
    if y > height - radius or y < 0 + radius:
        changeY = -changeY
    ellipse(x, y, 2*radius, 2*radius)
    
def mouseClicked():
    global changeX, changeY
    changeX = random(-10, 10)
    changeY = random(-10, 10)