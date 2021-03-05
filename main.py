import pgzero
from pgzero.builtins import Actor, animate, keyboard
playerimage = "diamond_s.png"
ballimage = "dodge-ball-brown"
player = Actor(playerimage)
balls = Actor(ballimage)

def draw():
    screen.fill("black")
    player.draw()
    balls.draw()



