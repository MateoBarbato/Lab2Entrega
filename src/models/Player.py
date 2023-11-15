import pygame
from Config import GRAVITY, PLAYERVELOCITY, SCREENHEIGHT, SCREENWIDTH


class Player:

    def __init__(self, image: pygame.image, x: int, y: int, width: int, height: int, screen: pygame.display) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.mask = pygame.mask.from_surface(self.image)
        self.screen = screen
        self.speedY = 0
        self.speedX = 2
        # self.velocityY = 0
        self.jumping = False

    def setPlayerSpeed(self, speed=1.5):
        self.speedX = speed

    def jump(self, state: bool):
        if state:
            self.speedY = -PLAYERVELOCITY
            self.jumping = True
            self.currentPos = self.rect.bottom
        else:
            self.jumping = False
            self.speedY = 0

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            if self.rect.left > 0:
                self.rect.move_ip(-self.speedX, 0)
        if key[pygame.K_d]:
            if self.rect.right < SCREENWIDTH:
                self.rect.move_ip(self.speedX, 0)

        if self.jumping == False:
            if self.rect.bottom > SCREENHEIGHT-5:
                pass
            elif self.rect.bottom != SCREENHEIGHT:

                self.rect.move_ip(0, GRAVITY)

                # return
        if self.jumping == True:
            self.rect.move_ip(0, self.speedY)

    def blitPlayer(self):
        self.screen.blit(self.image, self.rect)
