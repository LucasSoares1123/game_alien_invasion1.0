import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Classe geral para manipular o jogo"""

    def __init__(self):
        """Inicializa o jogo"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Invasão Alien")
        self.ship = Ship(self)

    def run_game(self):
        """Inicializa o loop principal do jogo"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Metodo acionado quando se aperta uma tecla ou mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.rect.x += 1  # move a nave para direita

    def _update_screen(self):
        """Atualiza as imagens na tela e muda para a proxima tela"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()  # Sempre mostra a tela mais recente


if __name__ == '__main__':  # Cria uma instancia e da um start no game
    ai = AlienInvasion()
    ai.run_game()
