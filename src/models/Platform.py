import pygame

from Config import ANIMATIONSPEED, TRAPSPIKES, TRAPTEST
from colors import GREEN
from spriteSheet import loadSprites


class Platform (pygame.sprite.Sprite):
    """
    Represents a platform in the game.

    Args:
        groups (list of pygame.sprite.Group): The groups to add the platform to.
        pos (tuple of int): The position of the platform.
        size (int): The size of the platform.
        screen (pygame.Surface): The screen to draw the platform on.
        isTrap (bool): Whether the platform is a trap.

    Attributes:
        image (pygame.Surface): The image of the platform.
        rect (pygame.Rect): The rectangle of the platform.
        screen (pygame.Surface): The screen to draw the platform on.
        size (int): The size of the platform.
        isTrap (bool): Whether the platform is a trap.
        trapOn (bool): Whether the trap is on.
        lastUpdate (int): The last time the trap was updated.
        spriteKeys (list of str): The keys to the sprites in the sprite sheet.
        sheet (str): The path to the sprite sheet.
        currentFrame (int): The current frame of the animation.
        trapOnSound (pygame.mixer.Sound): The sound that plays when the trap is turned on.
        animations (dict): A dictionary of animations.

    Methods:
        trapSound(): Plays the trap sound.
        setImage(image: pygame.Surface) -> pygame.Surface: Sets the image of the platform.
        animateTrap(): Animates the trap.
        update(): Updates the platform.
    """

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
        self.trapOnSound = TRAPSPIKES
        self.animations = loadSprites(
            self.sheet, size, size, 1, 8, self.spriteKeys)

        self.imageTrap = self.setImage(
            self.animations['trap'][self.currentFrame])

        self.rectTrap = self.imageTrap.get_rect(
            topleft=(pos[0], pos[1]-size))

    def trapSound(self):
        """Plays the trap sound."""
        self.trapOnSound.play()

    def setImage(self, image):
        """
        Sets the image of the platform.

        Args:
            image (pygame.Surface): The new image of the platform.

        Returns:
            pygame.Surface: The scaled image of the platform.
        """
        image = pygame.transform.scale(image, (self.size, self.size))
        return image

    def animateTrap(self):
        """Animates the trap."""
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
        """Updates the platform."""
        if self.isTrap:
            if self.trapOn:
                self.animateTrap()
                self.screen.blit(self.imageTrap, self.rectTrap)
