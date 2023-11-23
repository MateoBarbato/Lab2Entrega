import pygame


class Platform (pygame.sprite.Sprite):
    def __init__(self, groups, width, height, x, y) -> None:
        super().__init__(groups)
        # self.image = pygame.Surface((width, height), pygame.SRCALPHA, 32)
        self.image = pygame.Surface((width, height))
        # self.rect = self.image.get_rect(topleft=pos)
        self.rect = self.image.get_rect(topleft=(x, y))
        # self.image.fill((0, 0, 0))

    def draw(self):
        self.screen.blit(self.image, self.rect)
