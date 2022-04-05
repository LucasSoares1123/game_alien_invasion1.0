import pygame


class Ship:
    """Classe para controlar a nave espacial"""

    def __init__(self, ai_game):
        """Inicializa a nave em uma posição específica"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Carrega a imagem da nave e cria um Rect
        self.image = pygame.image.load('images/space_ship.bmp')
        self.rect = self.image.get_rect()

        # Começa com a nave na parte de baixo da tela
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Desenha a nave na atual localização"""
        self.screen.blit(self.image, self.rect)
