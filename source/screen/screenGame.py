from source.utils.background import BackgroundMoving
from source.player.player import Player
from source.player.status import Status
from source.player.score import Score
from source.enemy.enemySpawner import EnemySpawner
from source.powerUp.powerUpSpawner import PowerUpSpawner
from source.player.collisionDetector import CollisionDetector
import pygame


class ScreenGame:
    def __init__(self, screen):
        # pygame.init()  # <--- recrear el contenido de pantalla
        # screen = pygame.display.set_mode((800, 600))  # <--- crear una pantalla 800 x 600
        # pygame.display.set_caption("Galaga Refactorized - Revenge of Bombs")  # título
        # musica:
        # pygame.mixer.init()
        # pygame.mixer.music.load("music/bg_music.mp3")
        # pygame.mixer.music.play(-1) # <--- loop
        # juego
        self.screen = screen
        self.bg = BackgroundMoving(screen.get_width(), screen.get_height()) # infinito
        self.enemy_spawner = EnemySpawner() # generar los enemigos/bombas
        self.powerup_spawner = PowerUpSpawner() # genera los power_ups
        self.collision_detector = CollisionDetector() # colisionado bomba - misil
        self.player = Player(screen.get_height(), screen.get_width()) # posición
        self.status = Status() # <--- cant. de vidas
        self.score = Score() # <--- puntos
        self.score_number = 0 # <--- 0
        self.finished = False # <--- finalizado
        self.clock = pygame.time.Clock() # <--- iniciamos un reloj para la tasa de refresco

    def reset_game(self):
        self.player.set_movement_start() # regresarlo a su posicion
        self.player.bullet_manager.reset_bullet_manager() # regresamos las balas que haya tenido el juegador
        # reinicar las minas del juego...

    def change_difficulty_game(self, value):
        self.enemy_spawner.set_difficulty(value)

    def playGame(self):
        self.player.update()
        self.player.get_bullet_manager().update()
        self.enemy_spawner.update()
        self.enemy_spawner.draw(self.screen)
        self.powerup_spawner.update()
        self.powerup_spawner.draw(self.screen)
        self.player.draw(self.screen)
        self.player.get_bullet_manager().draw(self.screen) # dibujar las balas
        # detectar colisiones entre la listas de balas y de enemigos
        if self.collision_detector.check_collisions(self.enemy_spawner.get_enemies(), self.player.get_bullet_manager().get_bullets()):
            self.score_number += 1
        # verificar que el jugador haya colisonado con una mina
        if self.collision_detector.check_collisions_player(self.enemy_spawner.get_enemies(), self.player):
            # bajamos una vida y lo regresamos al inicio
            self.player.set_movement_start()
            # TODO: Darle inmortalidad al jugador por 2 segundos
        # colisiona con un powerup
        self.collision_detector.check_collisions_powerup(self.powerup_spawner.get_list(), self.player)
        # if self.score_number % 5 == 0:
            # self.enemy_spawner.change_difficulty()
        self.status.draw(self.screen, self.player.get_lives())
        self.score.draw(self.screen, self.score_number)

    def get_finished(self):
        return self.finished

    def set_finished(self, val, lives = 0):
        self.player.lives = lives
        self.finished = val

    def reset_score(self):
        self.score_number = 0

    def get_result(self):
        return self.player.is_alive()


    def get_score(self):
        return self.score_number

    def loop(self):
        while not self.get_finished():
            self.clock.tick(20)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.set_finished(True)
            self.screen.fill((0, 0, 0))# pintar el fondo 0,0,0
            self.bg.update(self.screen)
            self.playGame()
            if not self.player.is_alive():
                # print('Score final: ' + str(self.score_number))
                self.set_finished(True)
            pygame.display.update()
