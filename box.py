import pygame
from typing import Optional, Union

class BoxManager:
    def __init__(self) -> None:
        pass

class Border:
    def __init__(self, gap, colour) -> None:
        self.gap = gap * 2
        self.colour = colour

class Box:
    def __init__(self, size, pos, colour, border: Optional[Union[Border, pygame.Surface]]) -> None:
        self.size = size
        self.pos = pos
        self.colour = colour
        self.border = border
    
    def surface(self):
        return pygame.Surface((self.size[0], self.size[1]))
    
    def border_surface(self):
        return pygame.Surface((self.size[0] + self.border.gap, self.size[1] + self.border.gap))

    def render(self, surf: pygame.Surface):
        image = self.surface()
        image.fill(self.colour)

        outline = self.border_surface()
        outline.fill(self.border.colour)

        surf.blit(outline, (self.pos[0] - self.border.gap // 2, self.pos[1] - self.border.gap // 2))
        surf.blit(image, (self.pos[0], self.pos[1]))

class DialogueButton:
    def __init__(self, size, pos=(0, 0)) -> None:
        pass

class DialogueChoices:
    def __init__(self, size, pos=(0, 0)) -> None:
        pass

class DialoguePortrait:
    def __init__(self, size, pos=(0, 0)) -> None:
        pass