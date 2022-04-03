import sys
import pygame


class AlienInvasion:
    """Classe geral para manipular o jogo"""

    def __init__(self):
        """Inicializa o jogo"""
        pygame.init()
        self.screnn = pygame.display.set_mode((1200, 600))
        pygame.display.set_caption("Invasão Alien")

    def run_game(self):
        """Inicializa o loop principal do jogo"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                pygame.display.flip()  # Sempre mostra a tela mais recente


if __name__ == '__main__':  # Cria uma instancia e da um start no game
    ai = AlienInvasion()
    ai.run_game()
