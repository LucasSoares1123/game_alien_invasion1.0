import pygame
from pygame.sprite import Sprite

class Bullet:
    """Classe para atirar munição através da Nave"""
    def __init__(self, ai_game):
        """Cria uma munição na posição atual da Nave"""
        super().__init__()
        self.screem = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Cria rect para Munição na (0, 0) e então configura a posição correcta
        self.rect = pygame.Rect(0, 0, self.settings.screen_width, self.settings.screen_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Guarda a posição da Munição num valor decimal
        self.y = float(self.rect.y)

    def update(self):
        """Faz a munição se mover para cima"""
        # Atualiza a posição da munição de decimos em decimos
        self.y -= self.settings.bullet_speed

        # Atualiza a posição do Rect da munição
        self.rect.y = self.y

    def draw_bullet(self):
        """Dezenha a munição na tela"""
        pygame.draw.rect(self.screen, self.color, self.rect)
             
