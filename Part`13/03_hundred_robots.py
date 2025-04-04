import pygame
import pygame.event

pygame.init()
window = pygame.display.set_mode((640,480))

robot = pygame.image.load("robot.png")

window.fill((0,0,0))
y = 20
external_x = 20
x = 20

for i in range(10):
  external_x += 10
  x = external_x 
  y += 20

  for j in range(10):
    window.blit(robot,(x,y))
    x += robot.get_width()

pygame.display.flip()

while True:
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
