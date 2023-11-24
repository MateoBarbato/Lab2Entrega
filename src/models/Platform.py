import pygame


class Platform (pygame.sprite.Sprite):
    def __init__(self, groups, pos, size) -> None:
        super().__init__(groups)
        # self.image = pygame.Surface((width, height), pygame.SRCALPHA, 32)
        self.image = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        # self.rect = self.image.get_rect(topleft=pos)
        self.rect = self.image.get_rect(topleft=pos)
        # self.image.fill((190, 190, 0))
