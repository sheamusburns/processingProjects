
var turn = false,
numTilesX = 4,
numTilesY = 4,
tileW = 100,
tileH = 100,
tiles = [],
score = 0,
barH = 50,
tileD = 10,
padding = 30,
score = 0,
boppers = [];

function Tile(loc, h, w, d, angle, img_name){
  this.loc = loc;
  this.h = h;
  this.w = w;
  this.d = d;
  this.angle = 180;
  this.name = img_name;
  this.img = loadImage(img_name);
  this.angVel = 4;
  this.spinning = false;
  this.show = false;
  this.waitToAnnounce = false;
  this.matched = false;
  this.leaving = false;
  this.active = false;
  var that = this;
        
  this.spin = function(ann){
    if (!ann) ann = false;
    that.spinning = true;
    if (ann === 'announce'){
      that.waitToAnnounce = true;
    }
  }      
  this.render = function(){
    noStroke();
    translate(that.loc.x, that.loc.y, that.loc.z-that.d/2);
    rotateX(radians(that.angle));
    box(that.h, that.w, that.d);
    // translate(-50, -50, that.d/2+.1);
    // image(that.img, 0, 0, that.w, that.h);
    // translate(50, 50, -1*that.d/2 +.1);
    rotateX(-1*radians(that.angle));
    translate(that.loc.x*-1, that.loc.y*-1, (that.loc.z-that.d/2)*-1)
    if (that.spinning === true && that.show === false){
      that.angle += that.angVel;
      if (that.angle >=360){
        that.spinning = false;
        that.show = true;
        if (that.waitToAnnounce === true){
          turn.compare_picks();
          that.waitToAnnounce = false;
        }
      }
    }
    else if ( that.spinning === true && that.show === true ) {
      that.angle -= that.angVel;
      if (that.angle <= 180){
        that.spinning = false;
        that.show = false;
      }
    }
    if (that.leaving !== false){
      that.leave();
    }
  }
  
  this.leave = function(){
    if (that.leaving == 1){
      if (that.loc.z < that.d + 10){
        that.loc.z -= 2
      }
      else{ 
        that.leaving = 2
      }
    }
    if (that.leaving == 2){
      if (that.loc.y < height + tileH/2){
        that.loc.y += 3;
      }
      else{
        that.leaving = 3
      }
    }
    if (that.leaving == 3){}
  }
}



function setup() {
  createCanvas(tileW*numTilesX + padding*(numTilesX+1), tileH*numTilesY + barH + (numTilesY*padding)-1, WEBGL);
  initX = tileW/2 + padding;
  initY = tileH/2 + barH;
  
  
  for (var i = 0; i < numTilesX*numTilesY/2; i++) {
    boppers.push('jt' + i + '.jpg');
    boppers.push('jt' + i + '.jpg');
  }
  console.log(boppers);
  for (var t = 1; t < (numTilesX * numTilesY)+1; t++){
    tiles.push(new Tile(createVector(initX, initY, 0), tileW, tileH, tileD, 3, boppers.pop()));
    if (t % numTilesX === 0){
      initX = tileW/2 + padding;
      initY += tileH + padding;
    }
    else {
      initX += tileW + padding;
    }
  }
  console.log(tiles);
}

function draw() {
  background(120);
  translate(-1*width/2, -1*height/2)
  for (var p in tiles) {
    tiles[p].render();
  }
}

function Turn(){
  this.first_pick = false;
  this.second_pick = false;
  this.pick = function(p){
    if (!this.first_pick){
      this.first_pick = p;
      this.first_pick.spin();
    } else {
      this.second_pick = p;
      this.second_pick.spin('announce');
    }
  }
  this.reset = function(){
      this.first_pick.active = false;
      this.first_pick = false;
      this.second_pick.active = false;
      this.second_pick = false;
  }
  this.compare_picks = function(){
    if (this.first_pick.name == this.second_pick.name){
        print('yay');
        this.first_pick.leaving = 1;
        this.second_pick.leaving = 1;
        score += 1;
        this.reset();
    }
    else {
        print('noooo');
        this.first_pick.spin();
        this.second_pick.spin();
        this.reset();
    }
  }
}




function mouseClicked(){
  console.log(mouseX, mouseY);
  for (var t in tiles){
    if (mouseX < tiles[t].loc.x + tiles[t].w/2 && mouseX > tiles[t].loc.x - tiles[t].w/2 && mouseY < tiles[t].loc.y + tiles[t].h/2 && mouseY > tiles[t].loc.y - tiles[t].h/2){
      if (!turn && !tiles[t].active){
        turn = new Turn()
        turn.pick(tiles[t])
        tiles[t].active = true
      }
      else if (turn && !turn.second_pick && !tiles[t].active) {
        turn.pick(tiles[t])
        tiles[t].active = true
      }
    }
  }
}