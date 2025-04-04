# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
velocity = 1
robot = pygame.image.load("robot.png")

# function to always get new robots
def get_robots()-> list:
  robots = []
  
  # first fill the robots list with random sequence from 3-10
  for _ in range(randint(3,10)):
    # calculate x,y for each robot
    x = randint(60,window.get_width() - 60)
    y = randint(-86,-5)
    
    # move left or right if robot hits bottom
    if randint(0,1) == 0:
      v = -velocity
    else:
      v = velocity
    # add the robot
    robots.append([robot,x,v,y])

  return robots

robots = get_robots()
while True:
  
    window.fill((0, 0, 0))     
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        exit()

    # run through robot loop
    for cur_robot in robots:
      # if current robot is hitting bottom
      if cur_robot[3] + robot.get_height() >= 480:  
        # move the x left or right by adding velocity
        cur_robot[1] += cur_robot[2]
        # repeat the process once robot moves out of the screen
        if cur_robot[1] > 640 or cur_robot[1] < 0:
          # calculate x and y 
          cur_robot[1] = randint(60,window.get_width() - 60)
          cur_robot[3] = randint(-86,-5)
      else: 
        # add y for current_robot by adding velocity
        cur_robot[3] += velocity    
      
      # draw the robot
      window.blit(cur_robot[0],(cur_robot[1],cur_robot[3]))
    
    pygame.display.flip()
    clock.tick(60)
