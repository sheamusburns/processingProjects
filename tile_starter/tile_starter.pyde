import random as shuffle

boppers = []
turn = False
numTilesX = 4
numTilesY = 4
tileW = 100
tileH = 100
score = 0
barH = 50
tileD = 10
padding = 30
score = 0

for i in range(0, numTilesX*numTilesY/2):
    print(i)
    boppers.append('jt'+str(i)+'.jpg')
    boppers.append('jt'+str(i)+'.jpg')

shuffle.shuffle(boppers)

class Turn:
    def __init__(self):
        self.first_pick = False
        self.second_pick = False
        
    def pick(self, p):
        if not self.first_pick:
            self.first_pick = p
            self.first_pick.spin()
        else:
            self.second_pick = p
            self.second_pick.spin('announce')
            
    def reset(self):
        self.first_pick.active = False
        self.first_pick = False
        self.second_pick.active = False
        self.second_pick = False
        
    def compare_picks(self):
        global score
        if self.first_pick.name == self.second_pick.name:
            print('yay')
            self.first_pick.leaving = 1
            self.second_pick.leaving = 1
            score += 1
            self.reset()
        else:
            print('noooo')
            self.first_pick.spin()
            self.second_pick.spin()
            self.reset()
        
class Tile:
    def __init__(self, loc, h, w, d, angle, img_name):
        self.loc = loc
        self.h = h
        self.w = w
        self.d = d
        self.angle = 180
        self.name = img_name
        self.img = loadImage(img_name)
        self.angVel = 4
        self.spinning = False
        self.show = False
        self.waitToAnnounce = False
        self.matched = False
        self.leaving = False
        self.active = False
        
    def spin(self, ann = False):
        self.spinning = True
        if ann == 'announce':
            self.waitToAnnounce = True
            
    def render(self):
        noStroke()
        translate(self.loc.x, self.loc.y, self.loc.z-self.d/2)
        rotateX(radians(self.angle))
        box(self.h, self.w, self.d)
        translate(-50, -50, self.d/2+.1)
        image(self.img, 0, 0, self.w, self.h)
        translate(50, 50, -1*self.d/2 +.1)
        rotateX(-1*radians(self.angle))
        translate(self.loc.x*-1, self.loc.y*-1, (self.loc.z-self.d/2)*-1)
        if self.spinning == True and self.show == False:
            self.angle += self.angVel
            if self.angle >=360 :
                self.spinning = False
                self.show = True
                if self.waitToAnnounce == True:
                    turn.compare_picks()
                    self.waitToAnnounce = False
        elif self.spinning == True and self.show == True:
            self.angle -= self.angVel
            if self.angle <= 180:
                self.spinning = False
                self.show = False
        if self.leaving != False:
            self.leave()
    def leave(self):
        if self.leaving == 1:
            if self.loc.z < self.d + 10:
                self.loc.z -= 2
            else: self.leaving = 2
        if self.leaving == 2:
            if self.loc.y < height + tileH/2:
                self.loc.y += 3
            else:
                self.leaving = 3
        if self.leaving == 3:
            pass

def setup():
    global tiles, boppers
    tiles = []
    initX = tileW/2 + padding
    initY = tileH/2 + barH
    size(tileW*numTilesX + padding*(numTilesX+1), tileH*numTilesY + barH + (numTilesY*padding)-1, P3D)
    textSize(40)
    for i in range(1,(numTilesX * numTilesY) + 1):
        tiles.append(Tile(PVector(initX, initY, 0), tileW, tileH, tileD, 3, boppers.pop()))
        if i % numTilesX == 0:
            initX = tileW/2 + padding
            initY += tileH + padding
        else:
            initX += tileW + padding

def mouseClicked():
    global tiles, turn
    #check if it was clicked on a specific item
    # if it was, run the spin function on that item
    for t in tiles:
        if mouseX < t.loc.x + t.w/2 and mouseX > t.loc.x - t.w/2 and mouseY < t.loc.y + t.h/2 and mouseY > t.loc.y - t.h/2:
            if not turn and t.active is False:
                turn = Turn()
                turn.pick(t)
                t.active = True
            elif turn and not turn.second_pick and t.active is False:
                turn.pick(t)
                t.active = True
            
def draw():
    global tiles
    background(120)
    directionalLight(300, 300, 300, 0, 0, -1)
    ambientLight(200, 102, 102)
    lightSpecular(204, 204, 204)
    lights()
    for p in tiles:
        p.render()

    # working on score feature
    # translate(40, 80, 50)
    # fill(30)
    # text(str(score), 0, 0)
    # fill(255)
    
