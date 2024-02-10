import pygame
import sys

from box import Box, Border

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

pygame.init()
pygame.display.set_caption("Pygame Dialogue Box")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

box_width, box_height = 580, 180

testBox = Box(size=(box_width, box_height), pos=((SCREEN_WIDTH - box_width) // 2 , SCREEN_HEIGHT - box_height - 25), colour=(0, 0, 0), border=Border(5, (255, 255, 255)))

while True:
    screen.fill((0, 0, 0))

    testBox.render(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)