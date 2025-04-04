# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
robot1 = pygame.image.load("robot.png")
clock = pygame.time.Clock()
x = 0
y = 0
to_right = False
to_left = False
to_up = False
to_down = False

x1 = 0
y1 = 0
to_right1 = False
to_left1 = False
to_up1 = False
to_down1 = False

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
        if event.key == 119:
          to_up1 = True
        if event.key == 115:
          to_down1 = True
        if event.key == 97:
          to_left1 = True
        if event.key == 100:
          to_right1 = True

      if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
          to_left = False
        if event.key == pygame.K_RIGHT:
          to_right = False
        if event.key == pygame.K_UP:
          to_up = False
        if event.key == pygame.K_DOWN:
          to_down = False
        if event.key == 119:
          to_up1 = False
        if event.key == 115:
          to_down1 = False
        if event.key == 97:
          to_left1 = False
        if event.key == 100:
          to_right1 = False

      if event.type == pygame.QUIT:
        exit()

    if to_right and x + robot.get_width() <= 640:
        x += 2

    if to_right1 and x1 + robot.get_width() <= 640:
        x1 += 2
    
    if to_left and x - robot.get_width() >= -robot.get_width():
        x -= 2

    if to_left1 and x1 - robot.get_width() >= -robot.get_width():
        x1 -= 2

    if to_up and y - robot.get_height() >= -robot.get_height():
      y -= 2

    if to_up1 and y1 - robot1.get_height() >= -robot1.get_height():
      y1 -= 2

    if to_down and y + robot.get_height() <= 480:
      y += 2
    
    if to_down1 and y1 + robot1.get_height() <= 480:
      y1 += 2

    window.fill((0, 0, 0))
    window.blit(robot, (x,y))
    window.blit(robot1,(x1,y1))
    pygame.display.flip()
    
    clock.tick(60)
