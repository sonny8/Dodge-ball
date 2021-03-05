import pgzero
from pgzero.builtins import Actor, animate, keyboard

playerimage = "diamond_s.png"
ballimage = "dodge-ball-brown"
player = Actor(playerimage)
balls = Actor(ballimage)
WIDTH = 500
HEIGHT = WIDTH

def draw():
    screen.fill("black")
    player.draw()
    balls.draw()


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


