import random
from source.powerUp.powerUp import PowerUp


# Refactorización
# Ordenar el código de manera que sea legible en el futuro para otros programadores o para mí
# Se hace después de implementar SOLID
# No se modifican las funcianalidades

class PowerUpSpawner:
    x_vals = [i for i in range(60, 740, 60)]
    dy_vals = [i for i in range(1, 10)]

    def __init__(self):
        self.powerups = []

    def spawn(self):
        pu = PowerUp(random.choice(self.x_vals), random.choice(self.dy_vals))
        self.powerups.append(pu)

    def draw(self, screen):
        for pu in self.powerups:
            pu.draw(screen)

    def update(self):
        aleatorio = random.randint(1, 100) # [1, 100]
        print(aleatorio)
        if aleatorio % 100 == 0:
            self.spawn()
        for pu in self.powerups:
            pu.update()

    def get_list(self):
        return self.powerups
