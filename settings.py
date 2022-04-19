class Settings:
    """Classe para adicionar as configurações para o jogo"""
    def __init__(self):
        """Inicializa as configurações do jogo"""
        # configurações da Tela
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (0, 191, 255)

        # Configurações da Nave
        self.ship_speed = 1.5

        # Configurações da munição da Nave
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
