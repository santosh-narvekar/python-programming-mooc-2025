# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((640,480))

robot = pygame.image.load("robot.png")

window.fill((0,0,0))
y = 20
external_x = 20
x = 20

for i in range(1000):
    x = randint(0,640 - robot.get_width())
    y = randint(0,480 - robot.get_height())
    window.blit(robot,(x,y))
pygame.display.flip()

while True:
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
