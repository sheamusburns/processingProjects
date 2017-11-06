add_library('sound')
mic = None
amp = None

h = 0
vol = 0
sonics = []
easing = 0.05
easedVal = 0.00
    
def setup():
    frameRate(120)
    global mic, amp
    size(500, 200)
    mic = AudioIn(this, 0)
    mic.start()
    amp = Amplitude(this)
    amp.input(mic)
    
    
def draw():
    global easedVal
    background(100)
    vol = map(amp.analyze()*8, 0, 1, 0, 100)
    easedVal += (vol - easedVal) * easing
    print(vol)
    sonics.append(Sonic(easedVal, height))
    if sonics[0].x_loc > width:
            sonics.pop(0)
    for i in range(len(sonics)):
        sonics[i].draw_me()

class Sonic:
    def __init__(self, vol, scrn_height):
        self.x_loc = 0
        self.vol = vol
        self.scrn_height = scrn_height
    
    def draw_me(self):
        line(self.x_loc, self.scrn_height/2-self.vol, self.x_loc, self.scrn_height/2)
        self.x_loc += 1