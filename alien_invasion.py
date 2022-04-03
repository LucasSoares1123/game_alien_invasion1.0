import sys
import pygame
from settings import Settings


class AlienInvasion:
    """Classe geral para manipular o jogo"""

    def __init__(self):
        """Inicializa o jogo"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Invasão Alien")

    def run_game(self):
        """Inicializa o loop principal do jogo"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                pygame.display.flip()  # Sempre mostra a tela mais recente
                self.screen.fill(self.settings.bg_color)


if __name__ == '__main__':  # Cria uma instancia e da um start no game
    ai = AlienInvasion()
    ai.run_game()
