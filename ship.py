import pygame


class Ship:
    """Classe para controlar a nave espacial"""

    def __init__(self, ai_game):
        """Inicializa a nave em uma posição específica"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Carrega a imagem da nave e cria um Rect
        self.image = pygame.image.load('images/space_ship.bmp')
        self.rect = self.image.get_rect()

        # Começa com a nave na parte de baixo da tela
        self.rect.midbottom = self.screen_rect.midbottom

        # Guarda um valor decimal para a posição horizontal da Nave
        self.x = float(self.rect.x)

        # Flag de movimento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Atualiza o movimento da nave com base na Flag de movimento"""
        # Atualiza o valor de X da Nave, não do Rect
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        # Aqui sim atulaliza o Rect da Nave no self.x
        self.rect.x = self.x

    def blitme(self):
        """Desenha a nave na atual localização"""
        self.screen.blit(self.image, self.rect)


