from box import Box, DialogueButton, DialogueChoices, DialoguePortrait

class TreeManager:
    def __init__(self) -> None:
        pass

class Text:
    def __init__(self, text: str, size, pos=(0, 0), colour=None, speed=5, end=True) -> None:
        pass

class DialogueNode:
    def __init__(self, node_id: str, text: Text, choices, box: Box) -> None:
        pass