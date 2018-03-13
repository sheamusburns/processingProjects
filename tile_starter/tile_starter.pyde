import random as shuffle

class Tile:
    def __init__(self, loc, h, w, d, angle, img_name):
        self.loc = loc
        self.h = h
        self.w = w
        self.d = d
        self.angle = 180
        self.img = loadImage(img_name)
        self.angVel = random(1, 3)
        self.spinning = False
        self.show = False
    def spin(self):
        self.spinning = True
    def render(self):
        noStroke()
        translate(self.loc.x, self.loc.y, self.loc.z)
        rotateX(radians(self.angle))
        box(self.h, self.w, self.d)
        translate(-50, -50, 5.1)
        image(self.img, 0, 0, 100, 100)
        translate(50, 50, -5.1)
        rotateX(-1*radians(self.angle))
        translate(self.loc.x*-1, self.loc.y*-1, self.loc.z*-1)
        if self.spinning == True and self.show == False:
            self.angle += self.angVel
            if self.angle >=360 :
                self.spinning = False
                self.show = True
        elif self.spinning == True and self.show == True:
            self.angle -= self.angVel
            if self.angle <= 180:
                self.spinning = False
                self.show = False
boppers = []
for i in range(0, 13):
    boppers.append('jt'+str(i)+'.jpg')
    boppers.append('jt'+str(i)+'.jpg')
shuffle.shuffle(boppers)
print(boppers)

def setup():
    global tiles, boppers
    tiles = []
    initX = 50
    initY = 50
    size(500, 500, P3D)
    for i in range(1,26):
        print(i)
        print("length", len(boppers))
        if i is not 13:
            tiles.append(Tile(PVector(initX, initY, 0), 100, 100, 10, 3, boppers.pop()))
        if i % 5 == 0:
            initX = 50
            initY += 100
        else:
            initX += 100

def mouseClicked():
    global tiles
    #check if it was clicked on a specific item
    # if it was, run the spin function on that item
    for t in tiles:
        if mouseX < t.loc.x + t.w/2 and mouseX > t.loc.x - t.w/2 and mouseY < t.loc.y + t.h/2 and mouseY > t.loc.y - t.h/2:
            t.spin()
            
def draw():
    global tiles
    background(130)
    lights()
    for p in tiles:
        p.render()