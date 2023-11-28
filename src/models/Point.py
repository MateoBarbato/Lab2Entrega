from random import randint
import pygame
from Config import ADDPOINT, FRUIT1SHEET, FRUIT2SHEET, FRUIT3SHEET, SPRITEBUGSIZE

from spriteSheet import loadSprites


class Point(pygame.sprite.Sprite):
    """
    Represents a point object that can be spawned and collected to add points to the player's score.

    Attributes:
        size (int): The size of the point object.
        pointsToAdd (int): The number of points to add to the player's score when the point is collected.
        type (str): The type of point (red, yellow, or blue).
        isKilled (bool): Whether the point has been collected.
        currentFacing (str): The direction the point is facing ('idle').
        currentFrame (int): The current frame of the point's animation.
        animations (dict): A dictionary containing the point's animations for each direction.
        image (pygame.Surface): The current image of the point.
        mask (pygame.Mask): The mask of the point for collision detection.
        rect (pygame.Rect): The rectangle defining the position and size of the point.
        lastUpdate (int): The last time the point's animation was updated.
        animationSpeed (int): The speed of the point's animation.
        ammountOfFrames (int): The number of frames in the point's animation.
        pointSound (pygame.Sound): The sound effect to play when the point is collected.

    Methods:
        setImage(image: pygame.Surface) -> None: Sets the point's image.
        addPointSound() -> None: Plays the point collection sound effect.
        randoType() -> None: Randomly determines the point's type and points to add.
        animate() -> None: Updates the point's animation frame.
        update() -> None: Updates the point's state and position.
    """

    def __init__(self, groups, pos, size) -> None:
        """
        Initializes the Point object with the specified size and position.

        Args:
            groups (pygame.sprite.Group): The groups to add the point to.
            pos (tuple): The (x, y) coordinates of the point's position.
            size (int): The size of the point object.
        """
        super().__init__(groups)
        self.size = size
        self.pointsToAdd = 0
        self.randoType()
        self.key = ['idle']
        self.isKilled = False
        # animaciones
        self.currentFacing = 'idle'
        self.currentFrame = 0
        self.animations = loadSprites(
            self.sheet, SPRITEBUGSIZE, SPRITEBUGSIZE, 1, 4, self.key)
        self.image = self.setImage(
            self.animations[self.currentFacing][self.currentFrame])
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(pos[0]+size/2, pos[1]+size/2))
        self.lastUpdate = pygame.time.get_ticks()
        self.animationSpeed = 250
        self.ammountOfFrames = 4
        self.pointSound = ADDPOINT

    def setImage(self, image):
        """
        Sets the point's image to the specified surface.

        Args:
            image (pygame.Surface): The new image for the point.

        Returns:
            None
        """
        self.image = pygame.transform.scale(
            image, (self.size/1.5, self.size/1.5))
        return self.image

    def addPointSound(self):
        """
        Plays the point collection sound effect.
        """
        self.pointSound.play()

    def randoType(self):
        """
        Randomly determines the point's type and points to add.
        """
        self.randInt = randint(0, 2)
        if self.randInt == 0:
            self.sheet = FRUIT1SHEET
            self.type = 'red'
            self.pointsToAdd = 15
        elif self.randInt == 1:
            self.sheet = FRUIT2SHEET
            self.type = 'yellow'
            self.pointsToAdd = 25
        elif self.randInt == 2:
            self.sheet = FRUIT3SHEET
            self.type = 'blue'
            self.pointsToAdd = 35

    def animate(self):
        """
        Updates the point's animation frame.
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
        Updates the point's state and position.
        """
        if self.isKilled:
            # hacer algo
            self.kill()
        self.animate()
