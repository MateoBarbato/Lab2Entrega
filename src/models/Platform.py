import pygame

from Config import ANIMATIONSPEED, TRAPTEST
from colors import GREEN
from spriteSheet import loadSprites


class Platform (pygame.sprite.Sprite):
    def __init__(self, groups, pos, size, screen, isTrap=False,) -> None:
        super().__init__(groups)
        self.image = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect(topleft=pos)
        self.screen = screen
        self.size = size
        self.isTrap = isTrap
        self.trapOn = False
        self.lastUpdate = pygame.time.get_ticks()
        self.spriteKeys = ['trap']
        self.sheet = TRAPTEST
        self.currentFrame = 0
        self.animations = loadSprites(
            self.sheet, size, size, 1, 8, self.spriteKeys)

        self.imageTrap = self.setImage(
            self.animations['trap'][self.currentFrame])

        self.rectTrap = self.imageTrap.get_rect(
            topleft=(pos[0], pos[1]-size))

    def setImage(self, image):
        image = pygame.transform.scale(image, (self.size, self.size))
        return image

    def animateTrap(self):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdate > ANIMATIONSPEED:
            self.imageTrap = pygame.transform.scale(
                self.animations['trap'][self.currentFrame], (self.size, self.size))
            self.currentFrame += 1
            if self.currentFrame == 8:
                self.currentFrame = 0
                self.trapOn = False
            self.lastUpdate = currentTime

    def update(self):
        if self.isTrap:
            if self.trapOn:
                self.animateTrap()
                self.screen.blit(self.imageTrap, self.rectTrap)
