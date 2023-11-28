

from colors import BLACK, LAVENDER
from models.Button import Button


class LevelButton(Button):
    def __init__(self, width, height, x, y, text, screen, colorbackground=..., colorText=..., fontSize=20) -> None:
        super().__init__(width, height, x, y, text,
                         screen, colorbackground, colorText, fontSize)
