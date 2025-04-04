# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
clock = pygame.time.Clock()
x = 0
y = 0
to_right = False
to_left = False
to_up = False
to_down = False

while True:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          to_left = True
        if event.key == pygame.K_RIGHT:
          to_right = True
        if event.key == pygame.K_UP:
          to_up = True
        if event.key == pygame.K_DOWN:
          to_down = True

      if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
          to_left = False
        if event.key == pygame.K_RIGHT:
          to_right = False
        if event.key == pygame.K_UP:
          to_up = False
        if event.key == pygame.K_DOWN:
          to_down = False

      if event.type == pygame.QUIT:
        exit()
    
    if to_right and x + robot.get_width() <= 640:
        x += 2
    if to_left and x - robot.get_width() >= -robot.get_width():
        x -= 2
    
    if to_up and y - robot.get_height() >= -robot.get_height():
      y -= 2
    if to_down and y + robot.get_height() <= 480:
      y += 2

    window.fill((0, 0, 0))
    window.blit(robot, (x,y))
    pygame.display.flip()

    clock.tick(60)
