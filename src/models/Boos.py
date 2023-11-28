from random import randint
from tarfile import BLOCKSIZE
import pygame
from Config import BOOSSHEET, BULLETSIZE, ENEMYVELOCITY, GRAVITY, LIMITHEIGHTGROUND, LIMITWIDTHGROUND, SCREENHEIGHT, SCREENWIDTH, SPRITEBELLSPROUT, SPRITEBUGCOL, SPRITEBUGROW, SPRITEBUGSIZE, ANIMATIONSPEED, loadImage
from models.Bullet import Bullet

from spriteSheet import loadSprites


class Boss(pygame.sprite.Sprite):

    """
    Represents the boss character in the game.

    Attributes:
        x (int): The x-coordinate of the boss's position.
        y (int): The y-coordinate of the boss's position.
        speed (int): The speed of the boss.
        pos (tuple): The (x, y) coordinates of the boss's position.
        pointsToAdd (str): The number of points to add to the player's score when the boss is defeated.
        width (int): The width of the boss.
        height (int): The height of the boss.
        currentFrame (int): The current frame of the boss's animation.
        sheet (str): The path to the boss's sprite sheet.
        spriteKeys (list): A list of the animation keys for the boss.
        animations (dict): A dictionary containing the boss's animations for each direction.
        image (pygame.Surface): The current image of the boss.
        rect (pygame.Rect): The rectangle defining the position and size of the boss.
        mask (pygame.Mask): The mask of the boss for collision detection.
        screen (pygame.Surface): The screen surface to draw the boss on.
        lastUpdate (int): The last time the boss's animation was updated.
        lastUpdateShooting (int): The last time the boss fired a bullet.
        animationSpeed (int): The speed of the boss's animation.
        ammountOfFrames (int): The number of frames in the boss's animation.
        currentFacing (str): The direction the boss is facing.
        bullets (pygame.sprite.Group): The group of bullets the boss fires.
        falling (bool): Whether the boss is falling.

    Methods:
        setImage(image: pygame.Surface) -> None: Sets the boss's image.
        animate() -> None: Updates the boss's animation frame.
        bulletHell() -> None: Fires a barrage of bullets at the player.
        update() -> None: Updates the boss's state and position.
        draw() -> None: Draws the boss onto the screen.
    """

    def __init__(self, groups, bulletsGroup, x: int, y: int, width: int, height: int, screen: pygame.display, pointsToAdd: str) -> None:
        """
        Initializes the Boss object with the specified position, size, and screen.

        Args:
            groups (pygame.sprite.Group): The groups to add the boss to.
            bulletsGroup (pygame.sprite.Group): The group to add the boss's bullets to.
            x (int): The x-coordinate of the boss's position.
            y (int): The y-coordinate of the boss's position.
            width (int): The width of the boss.
            height (int): The height of the boss.
            screen (pygame.Surface): The screen surface to draw the boss on.
            pointsToAdd (str): The number of points to add to the player's score when the boss is defeated.
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
        self.sheet = BOOSSHEET
        self.spriteKeys = ['idle']
        self.animations = loadSprites(
            self.sheet, 200, 93, 1, 8, self.spriteKeys)
        self.image = self.setImage(self.animations['idle'][self.currentFrame])
        self.rect = self.image.get_rect(topleft=(width,  height*2))
        self.mask = pygame.mask.from_surface(self.image)
        self.screen = screen
        self.lastUpdate = pygame.time.get_ticks()
        self.lastUpdateShooting = pygame.time.get_ticks()
        self.animationSpeed = ANIMATIONSPEED/1.5
        self.ammountOfFrames = 8
        self.currentFacing = 'idle'
        self.bullets = bulletsGroup
        self.falling = False

    def setImage(self, image):
        """
        Scales and sets the boss's image.

        Args:
            image (pygame.Surface): The image to set.

        Returns:
            pygame.Surface: The scaled image.
        """
        self.image = pygame.transform.scale(image, (self.width, self.height))
        return self.image

    def animate(self):
        """
        Updates the boss's animation frame.
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
        Updates the boss's state and position.
        """
        self.animate()

    def draw(self):
        """
        Draws the boss onto the screen.
        """
        self.screen.blit(self.image, self.rect)
