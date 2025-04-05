# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint
pygame.init()
pygame.display.set_caption("Asteroids")

display = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")
rock = pygame.image.load("rock.png")

points = 0
x = 0
y = display.get_height() - robot.get_height()
velocity = 1
to_left = False
to_right = False
game_font = pygame.font.SysFont("Arial", 24)
clock = pygame.time.Clock()
rocks = []
    
for _ in range(randint(2,4)):
  x_pos = randint(200,display.get_width() - 200)
  y_pos = randint(-200,-rock.get_height())
  rocks.append([rock,x_pos,y_pos])
  
while True:
   
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        to_left = True
      if event.key == pygame.K_RIGHT:
        to_right = True

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT:
        to_left = False
      if event.key == pygame.K_RIGHT:
        to_right = False

    if event.type == pygame.QUIT:
        exit()
   
  if to_left and x - robot.get_width() >= -robot.get_width():
    x -= 2

  if to_right and x + robot.get_width() <= display.get_width():
    x += 2

  display.fill((0, 0, 0))
  total_rocks = len(rocks)
  counted_rocks = 0

  for rock in rocks:
    rock[2] += velocity
  
    if (rock[2] >= y and rock[2] <= y + robot.get_height() ) and (rock[1] >= x and rock[1] <= x + robot.get_width()):
      points += 1
      counted_rocks += 1
      #print("total rocks",total_rocks)
      #print("counted rocks:",counted_rocks)

      if counted_rocks == total_rocks:
        rocks = []
        for _ in range(randint(2,4)):
          x_pos = randint(200,display.get_width() - 200)
          y_pos = randint(-200,-rock[0].get_height())
          rocks.append([rock[0],x_pos,y_pos])
      else:
        rocks.remove(rock)
        
    else:      
      display.blit(rock[0],(rock[1],rock[2]))

      if rock[2] >= display.get_height():
        exit()
    
  text = game_font.render(f"Points: {points}", True, (255, 0, 0))
  display.blit(text, (600 - text.get_width(),10))
  display.blit(robot,(x,y))
  pygame.display.flip()
  clock.tick(60)
