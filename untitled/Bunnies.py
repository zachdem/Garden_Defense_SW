import pygame

class Bunnies (pygame.sprite.Sprite):
    def __init__(self, x, y):

        self.x = x

        self.y = y

        self.bunny = pygame.image.load("bunny.png")

    def render(self):
