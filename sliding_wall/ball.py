class Ball:
    def __init__(self, radius, locX, locY, col):
        self.radius = radius
        self.locX = locX
        self.locY = locY
        self.color = col
    
    def changeX(self, num):
        self.locX += num
        
    def changeY(self, num):
        self.locY += num
        
    def render(self):
        ellipseMode(RADIUS)
        ellipse(self.locX, self.locY, self.radius, self.radius)