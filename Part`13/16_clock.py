# WRITE YOUR SOLUTION HERE
import pygame
import math
from datetime import datetime

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 640, 480
CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 200
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

def draw_clock():
    SCREEN.fill(BLACK)

    # Get current time
    now = datetime.now()
    hour = now.hour 
    minute = now.minute
    second = now.second

    # Time display (24-hour format) at top-center
    time_str = now.strftime("%H:%M:%S")
    pygame.display.set_caption(time_str)

    # Draw red boundary
    pygame.draw.circle(SCREEN, RED, CENTER, RADIUS, 5)

    # Draw red center circle
    pygame.draw.circle(SCREEN, RED, CENTER, 8)

    # Calculate angles for hands
    sec_angle = math.radians((second / 60) * 360 - 90)
    min_angle = math.radians((minute / 60) * 360 - 90)
    hour_angle = math.radians(((hour + minute / 60) / 12) * 360 - 90)

    # Calculate hand positions
    sec_length = RADIUS - 30
    min_length = RADIUS - 60
    hour_length = RADIUS - 80

    sec_x = CENTER[0] + int(sec_length * math.cos(sec_angle))
    sec_y = CENTER[1] + int(sec_length * math.sin(sec_angle))

    min_x = CENTER[0] + int(min_length * math.cos(min_angle))
    min_y = CENTER[1] + int(min_length * math.sin(min_angle))

    hour_x = CENTER[0] + int(hour_length * math.cos(hour_angle))
    hour_y = CENTER[1] + int(hour_length * math.sin(hour_angle))

    # Draw hands in blue
    pygame.draw.line(SCREEN, BLUE, CENTER, (hour_x, hour_y), 5)
    pygame.draw.line(SCREEN, BLUE, CENTER, (min_x, min_y), 3)
    pygame.draw.line(SCREEN, BLUE, CENTER, (sec_x, sec_y), 2)

    pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    running = True
    while running:
        draw_clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(1)  
    pygame.quit()

if __name__ == "__main__":
    main()
