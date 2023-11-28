import pygame
from Config import ANIMATIONSPEED, BLOCKWIDTH, BULLETBOSS, BULLETPLANT, BULLETPLAYER, BULLETWATER, LIMITWIDTHGROUND, SCREENWIDTH, SPIRTESIZEMAINHEIGHT, SPIRTESIZEMAINWIDTH, SPRITEBUGCOL, loadImage

from spriteSheet import loadSprites


class Bullet(pygame.sprite.Sprite):
    """
    Class representing a bullet fired by the player or enemies.

    Attributes:
        groups (pygame.sprite.Group): The group(s) to which the bullet belongs.
        x (int): The x-coordinate of the bullet's position.
        y (int): The y-coordinate of the bullet's position.
        size (tuple): The width and height of the bullet's image.
        speed (int): The speed of the bullet.
        currentFacing (str): The direction the bullet is facing ('left' or 'right').
        currentFrame (int): The current frame of the bullet's animation.
        ammountOfFrames (int): The number of frames in the bullet's animation.
        spriteKeys (list): A list of the keys for the bullet's animations.
        isKilled (bool): Whether the bullet has been destroyed.
        lastUpdate (int): The time of the last animation update.
        lastUpdateKilling (int): The time of the last kill animation update.
        loopAmmountKilling (bool): Whether the kill animation has looped.

    Methods:
        animateDirection(key: str): Animates the bullet based on the specified direction.
        killanimated(key: str): Plays the bullet's destruction animation.
        setImage(image): Sets the bullet's image.
        update(): Updates the bullet's position and animation.
        draw(): Draws the bullet on the screen.
    """

    def __init__(self, groups, x, y, speed, size, type, currentFacing) -> None:
        """
        Initializes the bullet.

        Args:
            groups (pygame.sprite.Group): The group(s) to which the bullet belongs.
            x (int): The x-coordinate of the bullet's position.
            y (int): The y-coordinate of the bullet's position.
            speed (int): The speed of the bullet.
            size (tuple): The width and height of the bullet's image.
            type (str): The type of bullet ('plant', 'water', 'player', or 'boss').
            currentFacing (str): The direction the bullet is facing ('left' or 'right').
        """
        super().__init__(groups)
        self.x = x
        self.y = y
        self.size = size
        self.width = size[0]
        self.height = size[1]
        self.speed = speed
        self.currentFacing = currentFacing
        self.currentFrame = 0
        self.ammountOfFrames = SPRITEBUGCOL
        self.spriteKeys = ['left', 'rigth', 'dying']
        self.spriteRowLength = 4
        self.spriteRows = 3
        if type == 'plant':
            self.sheet = BULLETPLANT

        elif type == 'water':
            self.sheet = BULLETWATER

        elif type == 'player':
            self.sheet = BULLETPLAYER

        elif type == 'boss':
            self.sheet = BULLETBOSS
            self.spriteRows = 5
            self.spriteKeys = ['left', 'rigth', 'dying', 'up', 'down']

        self.animations = loadSprites(
            self.sheet, 32, 32, self.spriteRows, self.spriteRowLength, self.spriteKeys)
        self.image = self.setImage(
            self.animations[self.currentFacing][self.currentFrame])
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.lastUpdate = pygame.time.get_ticks()
        self.lastUpdateKilling = pygame.time.get_ticks()
        self.loopAmmountKilling = 0
        self.animationSpeed = ANIMATIONSPEED
        self.isKilled = False

    def animateDirection(self, key: str):
        """
        Animates the bullet based on the specified direction.

        Args:
            key (str): The direction to animate ('left' or 'right').
        """
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdate > self.animationSpeed:
            self.setImage(self.animations[key][self.currentFrame])
            self.currentFrame += 1
            if self.currentFrame == self.ammountOfFrames:
                self.currentFrame = 0
            self.lastUpdate = currentTime

    def killanimated(self, key):
        """
        Plays the bullet's destruction animation.

        Args:
            key (str): The direction to animate ('left' or 'right').
        """
        self.currentFacing = 'dying'
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdateKilling > 250:
            self.setImage(self.animations[key][self.currentFrame])
            self.currentFrame += 1
            self.rect.move_ip(0, 8)
            if self.currentFrame == self.ammountOfFrames:
                self.loopAmmountKilling = True
                self.currentFrame = 0
            self.lastUpdateKilling = currentTime
        if self.loopAmmountKilling == True:
            self.kill()

    def setImage(self, image):
        """
        Sets the bullet's image.

        Args:
            image (pygame.Surface): The image to set.

        Returns:
            The bullet's image.
        """
        self.image = pygame.transform.scale(image, (self.width, self.height))
        return self.image

    def update(self):
        """
        Updates the bullet's position and animation.
        """
        if self.isKilled == True:
            self.killanimated('dying')
        else:
            if self.currentFacing == 'left':
                self.rect.x += -self.speed
                self.animateDirection('left')

            if self.currentFacing == 'rigth':
                self.rect.x += self.speed
                self.animateDirection('rigth')

            if self.currentFacing == 'up':
                self.rect.y -= self.speed
                self.animateDirection('up')

            if self.currentFacing == 'down':
                self.rect.y += self.speed
                self.animateDirection('down')

    def draw(self):
        """
        Draws the bullet on the screen.
        """
        self.screen.blit(self.image, self.rect)
