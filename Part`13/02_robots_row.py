# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()

window = pygame.display.set_mode((640,480))

robot = pygame.image.load("robot.png")

window.fill((0,0,0))
window.blit(robot,(60,100))
window.blit(robot,(60 + robot.get_width(),100))
window.blit(robot,(60 + robot.get_width() + robot.get_width(),100))
window.blit(robot,(60 + robot.get_width() + robot.get_width() + robot.get_width(),100))
window.blit(robot,(60 + robot.get_width() + robot.get_width() + robot.get_width() + robot.get_width(),100))
window.blit(robot,(60 + robot.get_width() + robot.get_width() + robot.get_width() + robot.get_width() + robot.get_width(),100))
window.blit(robot,(60 + robot.get_width() + robot.get_width() + robot.get_width() + robot.get_width() + robot.get_width() + robot.get_width(),100))
window.blit(robot,(60 + robot.get_width() + robot.get_width() + robot.get_width() + robot.get_width() + robot.get_width() + robot.get_width() + robot.get_width(),100))
window.blit(robot,(60 + robot.get_width() + robot.get_width() + robot.get_width() + robot.get_width() + robot.get_width() + robot.get_width() + robot.get_width() + robot.get_width(),100))
window.blit(robot,(60 + robot.get_width() + robot.get_width() + robot.get_width() + robot.get_width() + robot.get_width() + robot.get_width() + robot.get_width() + robot.get_width() + robot.get_width(),100))

pygame.display.flip()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit()

