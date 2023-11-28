
from random import randint
import pygame
from Config import SPRITEBUGSIZE, VIDAPOINT

from spriteSheet import loadSprites


class Live(pygame.sprite.Sprite):
    """
    Represents a life object that can be collected to add extra lives to the player's count.

    Attributes:
        size (int): The size of the life object.
        key (list): A list containing the animation key for the life object.
        isKilled (bool): Whether the life object has been collected.
        currentFacing (str): The direction the life object is facing.
        currentFrame (int): The current frame of the life object's animation.
        sheet (str): The path to the life object's sprite sheet.
        animations (dict): A dictionary containing the life object's animation frames.
        image (pygame.Surface): The current image of the life object.
        mask (pygame.Mask): The mask of the life object for collision detection.
        rect (pygame.Rect): The rectangle defining the position and size of the life object.
        lastUpdate (int): The last time the life object's animation was updated.
        animationSpeed (int): The speed of the life object's animation.
        ammountOfFrames (int): The number of frames in the life object's animation.
        lifesToAdd (int): The number of lives to add to the player's count when the life object is collected.

    Methods:
        setImage(image: pygame.Surface) -> None: Sets the life object's image.
        animate() -> None: Updates the life object's animation frame.
        update() -> None: Updates the life object's state and position.
    """

    def __init__(self, groups, pos, size) -> None:
        """
        Initializes the Life object with the specified position and size.

        Args:
            groups (pygame.sprite.Group): The groups to add the life object to.
            pos (tuple): The (x, y) coordinates of the life object's position.
            size (int): The size of the life object.
        """
        super().__init__(groups)
        self.size = size
        self.key = ['idle']
        self.isKilled = False
        # animaciones
        self.currentFacing = 'idle'
        self.currentFrame = 0
        self.sheet = VIDAPOINT
        self.animations = loadSprites(
            self.sheet, SPRITEBUGSIZE, SPRITEBUGSIZE, 1, 4, self.key)
        self.image = self.setImage(
            self.animations[self.currentFacing][self.currentFrame])
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(pos[0]+size/2, pos[1]+size/2))
        self.lastUpdate = pygame.time.get_ticks()
        self.animationSpeed = 250
        self.ammountOfFrames = 4
        self.lifesToAdd = 1

    def setImage(self, image):
        """
        Scales and sets the life object's image.

        Args:
            image (pygame.Surface): The image to set.

        Returns:
            pygame.Surface: The scaled image.
        """
        self.image = pygame.transform.scale(
            image, (self.size/1.5, self.size/1.5))
        return self.image

    def animate(self):
        """
        Updates the life object's animation frame.
        """
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdate > self.animationSpeed:
            self.setImage(
                self.animations[self.currentFacing][self.currentFrame])
            self.currentFrame += 1
            if self.currentFrame == self.ammountOfFrames:
                self.currentFrame = 0
            self.lastUpdate = currentTime

    def update(self):
        """
        Updates the life object's state and position.
        """
        if self.isKilled:
            # hacer algo
            self.kill()
        self.animate()
