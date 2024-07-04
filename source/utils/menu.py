import pygame
import random
from source.utils.ui import Button


class Menu:
    def __init__(self, screen):
        # imagen generada con: https://logo.com/editor/
        __slots__ = ['x_random', 'y_random']
        self.image_logo = pygame.image.load('images/logo.png')  # imagen
        SCALE_FACTOR = 0.25
        self.image_logo = pygame.transform.scale_by(self.image_logo, SCALE_FACTOR) # escalar la imagen
        self.x_random = 0
        self.y_random = 0
        self.screen = screen
        self.h = screen.get_height() // 8
        self.w = screen.get_width() // 8
        self.image_spark = pygame.image.load('images/spark_1.png') # destello
        self.spawn_spark() # creando aleatoriamente los valores X e Y.
        self.button_play = Button(320, 400, "JUGAR") # objeto de la clse Button
        self.menu_finished = False # boton Jugar ha sido presionado

    def get_menu_finished(self):
        return self.menu_finished # obtener el valor booleano de menu_finished

    def events(self):
        if self.button_play.clicked: # si el boton play es tocado, cambiar menu_finished a True
            self.menu_finished = True

    def spawn_spark(self):
        # x_random = 5, y_random = 6 # se quede por un periodo de tiempo
        random_number = random.randint(1, 100) # aleatorio entre 1 y 100
        if random_number % 20 == 0: # si el numero es divisible entre 20...
            self.x_random = random.randint(10, self.w * 8) # generar un nuevo x_random 200
            self.y_random = random.randint(5, self.h * 8) # generar un nuvo valor para y_random 90

    def update(self):
        self.button_play.update()
        self.spawn_spark() # generar los X e Y de spark

    def draw(self):
        #dibujamos el logo
        self.screen.blit(self.image_logo, [self.w, self.h, self.image_logo.get_width(), self.image_logo.get_height()])
        # dibujando el spark
        self.screen.blit(self.image_spark, [self.x_random,self.y_random,self.image_spark.get_width(),self.image_spark.get_height()])
        # boton play
        self.button_play.draw(self.screen)


