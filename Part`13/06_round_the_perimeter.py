# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
velocity = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
   
    x += velocity
    
    if velocity > 0 and x + robot.get_width() >= 640:
        x = 640 - robot.get_width()
        y += velocity
        #print(y)
        #print(velocity)
        #print(robot.get_height())

    #print("external y",y)
    #print("external velocity", velocity)
    #print("external robo height: ",robot.get_height())
    #print("x",x)

    if velocity > 0 and y + robot.get_height() >= 480:
        y = 480 - robot.get_height()
        velocity = -velocity
    
    if velocity < 0 and x <= 0:
        y += velocity
        x = 0
        if y <= 0:
            velocity = -velocity

    clock.tick(60)
