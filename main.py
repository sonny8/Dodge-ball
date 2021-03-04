import pgzero
from pgzero.builtins import Actor, animate, keyboard
path = "C:/Users/User/Desktop/Github/Programs/Dodge-ball/images/diamond_s.png"
player = Actor(path)

def draw():
    screen.fill("black")
    player.draw()



