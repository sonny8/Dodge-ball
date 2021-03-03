import pygame
import sys
pygame.init()
wind=pygame.display.set_mode((750,650))
pygame.display.set_caption("Dodge Ball")

while True:
         for eve in pygame.event.get():
              if eve.type==pygame.QUIT:
                   pygame.quit()
                   sys.exit()

player = Actor("diamond_s.png")

def draw():
    screen.fill("black")
    player.draw()


