import pygame
import sys
from image_utils import *

from box import *
from dialogue_box import DialogueBox

SCREEN_SIZE = (640, 480)
BOX_SIZE = (580, 180)

pygame.init()
pygame.display.set_caption("Pygame Dialogue Box")
screen = pygame.display.set_mode((SCREEN_SIZE[0], SCREEN_SIZE[1]))
clock = pygame.time.Clock()


testBox = Box((BOX_SIZE[0], BOX_SIZE[1]), (0, 0, 0), Border(5, (255, 255, 255)))

testImage = load_image('portraits/sansface.png', (150, 150))
testPortrait = PortraitBox((testImage.get_width(), testImage.get_height()), testImage, (0, 0, 0), None)

dialogue1 = DialogueBox(testBox, ((SCREEN_SIZE[0] - BOX_SIZE[0]) // 2, (SCREEN_SIZE[1] - BOX_SIZE[1] - 25)), 
                        testPortrait, (20, 15))

#comicsansms

while True:
    screen.fill((0, 0, 0))
    dialogue1.render(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    pygame.display.update()
    clock.tick(60)