import pgzero
from pgzero.builtins import Actor, animate, keyboard
import time
playerimage = "resizeimage"
ballimage = "dodge-ball-brown"
bgimage = "background1"
player = Actor(playerimage)
balls = Actor(ballimage)
bg = Actor("background1")
WIDTH = 490
HEIGHT = 450

def draw():
    localtime = time.localtime(time.time())

    hour = localtime[3]
    if hour > 5 and hour < 12:

        screen.fill("lightblue")

    if hour > 17 and hour < 24:
        screen.fill("darkblue")




    bg.x = 250

    bg.draw()
    player.draw()





def update():



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
