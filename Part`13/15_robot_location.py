# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint
pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
target_x = 0
target_y = 0

clock = pygame.time.Clock()

while True: 
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        target_x = event.pos[0]
        target_y = event.pos[1]

        if target_x > x and target_x < x+robot.get_width() and target_y > y and target_y < y+robot.get_width():
           x = randint(0,window.get_width() - 50)
           y = randint(0,window.get_height() - 86)
   
      if event.type == pygame.QUIT:
         exit()
    
    window.fill((0, 0, 0)) 
    window.blit(robot,(x, y))
    pygame.display.flip()
    
    clock.tick(60)

