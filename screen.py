import pygame


class Screen:

    def __init__(self):
        self.image = pygame.image.load('images/background.jpg')
        self.rect = self.image.get_rect()
        self.screen = pygame.display.set_mode(
            (self.rect.width, self.rect.height))
        pygame.display.set_caption("Alien Invasion")

    def blit_me(self):
        self.screen.blit(self.image, self.rect)
