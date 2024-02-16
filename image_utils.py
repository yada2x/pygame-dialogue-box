import pygame
import os

BASE_IMG_PATH = 'data/'
def load_image(path, scale=None) -> pygame.Surface:
    image = pygame.image.load(BASE_IMG_PATH + path).convert()
    image.set_colorkey((0, 0, 0))
    if scale != None:
        return pygame.transform.scale(image, scale)
    return image

def load_images(path, scale=None) -> list[pygame.Surface]:
    images = []
    for i_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image(path + '/' + i_name, scale))
    return images