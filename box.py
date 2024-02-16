import pygame
from typing import Optional, Union

class Border:
    def __init__(self, gap, colour) -> None:
        self.gap = gap * 2
        self.colour = colour

class Box:
    def __init__(self, size, boxColour, borderImage: Optional[Union[Border, pygame.Surface, None]]) -> None:
        self.size = size
        self.pos = (0, 0)
        self.boxColour = boxColour
        self.borderOn = True if isinstance(borderImage, Border) else False
        self.borderImage = borderImage

    def setPos(self, x, y):
        self.pos = (x, y)

    def getWidth(self):
        return self.size[0]

    def getHeight(self):
        return self.size[1]

    def getX(self):
        return self.pos[0]

    def getY(self):
        return self.pos[1]

    def surface(self):
        return pygame.Surface((self.size[0], self.size[1]))
    
    def border_surface(self):
        return pygame.Surface((self.size[0] + self.borderImage.gap, self.size[1] + self.borderImage.gap))

    def render(self, surf: pygame.Surface):
        image = self.surface()
        image.fill(self.boxColour)

        if self.borderImage != None and self.borderOn:
            outline = self.border_surface()
            outline.fill(self.borderImage.colour)
            surf.blit(outline, (self.pos[0] - self.borderImage.gap // 2, self.pos[1] - self.borderImage.gap // 2))
        
        surf.blit(image, (self.pos[0], self.pos[1]))

        if self.borderImage != None and not self.borderOn: # test this later, see if transparency works, should blit a surface
            surf.blit(self.borderImage, (self.pos[0], self.pos[1]))

class Portrait(Box):
    def __init__(self, size, portrait: pygame.Surface, boxColour, borderImage: Optional[Union[Border, pygame.Surface]]) -> None:
        super().__init__(size, boxColour, borderImage)
        self.portrait = portrait

    def render(self, surf: pygame.Surface):
        super().render(surf)
        surf.blit(self.portrait, (self.pos[0], self.pos[1]))

class DialogueButton:
    def __init__(self, size, pos=(0, 0)) -> None:
        pass

class DialogueChoices:
    def __init__(self, size, pos=(0, 0)) -> None:
        pass