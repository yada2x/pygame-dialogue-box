import pygame
from box import *

class DialogueBox:
    def __init__(self, mainBox: Box, mainPos: tuple[int, int], portraitBox: PortraitBox, portraitPos: tuple[int, int]) -> None:
        self.mainBox = mainBox 
        self.mainPos = mainPos # Relative to the game screen
        self.mainBox.setPos(self.mainPos[0], self.mainPos[1])

        self.portraitBox = portraitBox
        self.portraitPos = portraitPos # Relative to mainPos
        self.portraitBox.setPos(self.portraitPos[0] + self.mainPos[0], self.portraitPos[1] + self.mainPos[1])

        # self.textBox = textBox # Implement later
        # self.textPos = textPos # Relative to mainPos
    
    def render(self, surf: pygame.Surface):
        self.mainBox.render(surf)
        self.portraitBox.render(surf)