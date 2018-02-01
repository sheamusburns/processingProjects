class Wall:
    def __init__(self, w, h, locX, locY, velX, velY, basicVel):
        self.w = w
        self.h = h
        self.position = PVector(locX, locY)
        self.velX = velX
        self.velY = velY
        self.basicVel = basicVel
        
    def render(self):
        rectMode(CENTER)
        self.position.x += self.velX
        self.position.y += self.velY
        self.checkBoundaryCollision()
        rect(self.position.x, self.position.y, self.w, self.h)
    
    def checkBoundaryCollision(self):
        # print('checkingBoundary')
        if self.position.x + self.w/2 >= width:
            self.changeDirection('left')
        if self.position.x - self.w/2 <= 0:
            self.changeDirection('right')
            
    def arrowPressed(self):
        if keyCode == 37:
            self.changeDirection('left')
        if keyCode == 39:
            self.changeDirection('right')
                    
    def changeDirection(self, dir):
        if dir == 'left':
            self.velX = -1 * self.basicVel
        if dir == 'right':
            self.velX = 1 * self.basicVel
        # print(self.velX, self.velY)
    
    def checkCollision(self, other):
        print(PVector.sub(other.position, self.position))
        # subtract the vectors of self and ball