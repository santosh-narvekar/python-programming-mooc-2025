# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
robot1 = pygame.image.load("robot.png")

x = 0
y = 50
x1 = 0
y1 = robot.get_height() + 70

velocity = 1
velocity1 = 1
clock = pygame.time.Clock()

while True: 
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        exit()
    
    window.fill((0, 0, 0))
    window.blit(robot,(x, y))
    window.blit(robot1,(x1,y1))
    pygame.display.flip()
    
    x += velocity
    if velocity > 0 and x + robot.get_width() >= 640:
        velocity = -velocity
    if velocity < 0 and x <= 0:
        velocity = -velocity

    
    x1 += velocity1 * 2
    
    if velocity1 > 0 and x1 + robot1.get_width() >= 640:
        velocity1 = -velocity1

    if velocity1 < 0 and x1 <= 0:
        velocity1 = -velocity1

    clock.tick(60)
