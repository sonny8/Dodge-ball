import pgzero
from pgzero.builtins import Actor, animate, keyboard
import time
import random
playerimage = "diamond_s"
ballimage = "dodge-ball-brown"
bgimage = "background1"
player = Actor(playerimage)
ball = Actor(ballimage)
bg = Actor("background1")
WIDTH = 490
HEIGHT = 450
fail = False
ball.center = WIDTH / 2, HEIGHT / 2
def draw():
    global fail
    localtime = time.localtime(time.time())

    hour = localtime[3]
    if hour > 5 and hour < 12:

        screen.fill("lightblue")

    if hour > 17 and hour < 24:
        screen.fill("darkblue")
        
    if fail:
        screen.fill("red")
        
    




    bg.x = 250

    bg.draw()
    player.draw()
    ball.draw()




xspeed = random.randint(0,5)
yspeed =random.randint(0,5)

def update():
    
    
    global xspeed, yspeed, fail
    
    ranpro_y = random.randint(-1,1)
    ranpro_x = random.randint(-1,1)
    
    xspeed+= ranpro_x
    yspeed += ranpro_y
    ball.x += xspeed
    ball.y += yspeed
    
    if xspeed > 7:
        xspeed = 3
    if xspeed < -7:
        xspeed = -3
        
        
    if yspeed > 7:
        yspeed = 3
        
    if yspeed < -7:
        yspeed = -3
    
    if player.colliderect(ball):
        sounds.eep.play()
        fail = True
        
        
        

    
    
    if keyboard.right:
        player.x += 5
    if keyboard.left:
        player.x += -5

    if keyboard.up:
        player.y += -5

    if keyboard.down:
        player.y += 5

    if player.left > WIDTH:
        player.right = 0
    if player.right < 0:
        player.left = WIDTH

    if player.bottom < 0:
        player.top = HEIGHT
        bg.x = 250
        bg.image = "background1"

        bg.draw()


    if player.top > HEIGHT:
        player.bottom = 0
        bg.image = "ground (3)"
        bg.y = 250
        bg.draw()

    if player.y > HEIGHT and bg.image == "ground (3)":
        player.y = HEIGHT
        
    if ball.left > WIDTH:
        ball.right = 0
        
    if ball.right < 0:
        ball.left = WIDTH
    if ball.bottom < 0:
        ball.top = HEIGHT
        
    if ball.top > HEIGHT:
        ball.bottom = 0
