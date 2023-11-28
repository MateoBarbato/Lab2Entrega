from random import randint
from tarfile import BLOCKSIZE
import pygame
from Config import BULLETSIZE, DAMAGEENEMY, ENEMYVELOCITY, GRAVITY, LIMITHEIGHTGROUND, LIMITWIDTHGROUND, SCREENHEIGHT, SCREENWIDTH, SHOOT, SPRITEBELLSPROUT, SPRITEBUGCOL, SPRITEBUGROW, SPRITEBUGSIZE, ANIMATIONSPEED, loadImage
from models.Bullet import Bullet

from spriteSheet import loadSprites


class BugStatic(pygame.sprite.Sprite):
    """
    Class representing a static enemy bug within the game.

    Attributes:
        groupsVar (pygame.sprite.Group): The group(s) to which the bug belongs.
        x (int): The x-coordinate of the bug's position.
        y (int): The y-coordinate of the bug's position.
        speed (int): The bug's horizontal movement speed.
        pos (tuple): The bug's position as a tuple.
        pointsToAdd (str): The type of element the bug represents ('fire', 'water', etc.).
        width (int): The width of the bug's image.
        height (int): The height of the bug's image.
        currentFrame (int): The current frame of the bug's animation.
        sheet (str): The path to the bug's sprite sheet.
        spriteKeys (list): A list of the keys for the bug's animations.
        animations (dict): A dictionary containing the bug's animations.
        image (pygame.Surface): The current image of the bug.
        rect (pygame.Rect): The bug's rectangle.
        mask (pygame.mask): The bug's collision mask.
        screen (pygame.Surface): The game's screen.
        lastUpdate (int): The time of the last animation update.
        animationSpeed (int): The speed of the bug's animation.
        ammountOfFrames (int): The number of frames in the bug's animation.
        currentFacing (str): The direction the bug is currently facing ('left' or 'right').
        bullets (pygame.sprite.Group): The group of bullets fired by the bug.
        falling (bool): Whether the bug is currently falling.
        direction (pygame.math.Vector2): The bug's direction of movement.
        gravity (float): The force of gravity acting on the bug.

    Methods:
        delBug(): Removes the bug from the game.
        setImage(image): Sets the bug's image.
        apply_gravity(): Applies gravity to the bug.
        animateDirection(): Animates the bug based on its current facing direction.
        update(): Updates the bug's state.
        draw(): Draws the bug on the screen.
    """

    def __init__(self, groups, bulletsGroup, x: int, y: int, width: int, height: int, screen: pygame.display, pointsToAdd: str) -> None:
        """
        Initializes the bug.

        Args:
            groups (pygame.sprite.Group): The group(s) to which the bug belongs.
            bulletsGroup (pygame.sprite.Group): The group to which the bug's bullets belong.
            x (int): The x-coordinate of the bug's position.
            y (int): The y-coordinate of the bug's position.
            width (int): The width of the bug's image.
            height (int): The height of the bug's image.
            screen (pygame.Surface): The game's screen.
            pointsToAdd (str): The type of element the bug represents ('fire', 'water', etc.).
        """
        super().__init__(groups)
        self.x = x
        self.y = y
        self.speed = 1
        self.pos = (x, y)
        self.pointsToAdd = pointsToAdd
        self.width = width
        self.height = height
        self.currentFrame = 0
        self.sheet = SPRITEBELLSPROUT
        self.spriteKeys = ['down', 'rigth', 'left']
        self.animations = loadSprites(
            self.sheet, SPRITEBUGSIZE, SPRITEBUGSIZE, SPRITEBUGROW, SPRITEBUGCOL, self.spriteKeys)
        self.image = self.setImage(self.animations['down'][self.currentFrame])
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)
        self.screen = screen
        self.lastUpdate = pygame.time.get_ticks()
        self.lastUpdateShooting = pygame.time.get_ticks()
        self.animationSpeed = ANIMATIONSPEED
        self.ammountOfFrames = SPRITEBUGCOL
        self.currentFacing = 'left'
        self.bullets = bulletsGroup
        self.falling = True
        self.direction = pygame.math.Vector2(0, 0)
        self.gravity = 0.72
        self.firstTimeFalling = True
        self.Shoot = SHOOT
        self.dyingsound = DAMAGEENEMY

    def randDirection(self):
        pass

    def shootSound(self):
        """Plays the shoot sound."""
        self.Shoot.play()

    def dyingSound(self):
        """Plays the dying sound."""
        self.dyingsound.play()

    def setImage(self, image):
        """
        Sets the bug's image.

        Args:
            image (pygame.Surface): The image to set.

        Returns:
            The bug's image.
        """
        self.image = pygame.transform.scale(image, (self.width, self.height))
        return self.image

    def apply_gravity(self):
        """
        Applies gravity to the bug.
        """
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def animateDirection(self):
        """
        Animates the bug based on its current facing direction.
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
        Updates the bug's state.

        This method updates the bug's position and animation.
        """
        if self.x > LIMITWIDTHGROUND/2:
            self.animateDirection()
            self.currentFacing = 'left'
        else:
            self.animateDirection()
            self.currentFacing = 'rigth'

    def draw(self):
        """
        Draws the bug on the screen.
        """
        self.screen.blit(self.image, self.rect)
