import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Uma classe para repressentar uma nave alien de frota"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game

        # Carrega a imagem
        self.image = pygame.image.load('images/ship1.bmp')
        self.rect = self.image.get_rect()

        # Começa com a nave alien no too da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição exata da nave alien
        self.x = float(self.rect.x)

