import pygame
from typing import Optional, Union

# Add ButtonBox and ChoiceBox
class Border:
    def __init__(self, gap: int, colour: tuple[int, int, int]) -> None:
        self.gap = gap * 2
        self.colour = colour

class Box:
    def __init__(self, size, boxFill: Optional[Union[tuple[int, int, int], pygame.Surface]], borderImage: Optional[Union[Border, pygame.Surface, None]]) -> None:
        self.size = size
        self.pos = (0, 0)
        
        self.colourOn = False if isinstance(boxFill, pygame.Surface) else True
        self.boxFill = boxFill

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

    def boxSurface(self):
        image = pygame.Surface((self.size[0], self.size[1]))
        image.fill(self.boxFill)
        return image
    
    def borderSurface(self):
        image = pygame.Surface((self.size[0] + self.borderImage.gap, self.size[1] + self.borderImage.gap))
        image.fill(self.borderImage.colour)
        return image

    def render(self, surf: pygame.Surface):
        if self.colourOn: # If self.boxFill is a colour, get its surface
            box = self.boxSurface()
        else:
            box = self.boxFill

        if self.borderOn: # If self.borderImage is a border, get its surface
            border = self.borderSurface()
        else:
            border = self.borderImage

        # Render border as Border
        if self.borderOn:
            surf.blit(border, (self.pos[0] - self.borderImage.gap // 2, self.pos[1] - self.borderImage.gap // 2))
        
        # Render box
        surf.blit(box, (self.pos[0], self.pos[1]))

        # Render border as Image (surface), test if this works later. Concerns about render order
        if not self.borderOn and self.borderImage != None: 
            surf.blit(self.borderImage, (self.pos[0], self.pos[1]))

class PortraitBox(Box):
    def __init__(self, size, portrait: pygame.Surface, boxColour, borderImage: Optional[Union[Border, pygame.Surface]]) -> None:
        super().__init__(size, boxColour, borderImage)
        self.portrait = portrait

    def render(self, surf: pygame.Surface):
        super().render(surf)
        surf.blit(self.portrait, (self.pos[0], self.pos[1]))
class TextBox:
    def __init__(self, text: str, char_size, ) -> None:
        pass