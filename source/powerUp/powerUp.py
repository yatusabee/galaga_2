from source.enemy.enemy import Enemy
import pygame
import random


class PowerUp(Enemy):
    def __init__(self, x, dy):
        super().__init__(x, dy)
        aleatorio = random.randint(1, 2) # valor entero aleatorio entre 1 y 2
        self.typePowerUp = None
        if aleatorio <= 1:
            self.imagen = pygame.image.load('images/powerup_bullets.png')
            self.imagen = pygame.transform.scale_by(self.imagen, 0.3)
            self.typePowerUp = 'PowerUpBullet'
        else:
            self.imagen = pygame.image.load('images/powerup_movement.png')
            self.imagen = pygame.transform.scale_by(self.imagen, 0.4)
            self.typePowerUp = 'PowerUpLife'
        self.rect = self.imagen.get_rect()
        self.rect.topleft = (self.x, self.y)

    def getTypePowerUp(self):
        return self.typePowerUp
