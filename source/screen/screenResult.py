import pygame
from source.utils.ui import Button

class ScreenResult:
    def __init__(self, width, height, win=False, score=0):
        self.half_width = width // 2
        self.half_height = height // 2
        self.center = (self.half_width, self.half_width)
        self.font = pygame.font.SysFont(None, 40)
        if win:
            self.text = self.font.render("GANASTE!!! Score: " + str(score), True, (0, 255, 0))
            # self.img = pygame.image.load('images/astronauta_ganaste.jpeg')
        else:
            self.text = self.font.render("Perdiste! Score: " + str(score), True, (255, 0, 0))
            # self.img = pygame.image.load('images/imagen_perdiste.jpg')
        self.text_rect = self.text.get_rect(center=(self.half_width, self.half_width))
        # self.img_rect = self.img.get_rect(center=(self.half_width, self.half_height // 2))
        
        self.text_name = self.font.render("\ -_- /", True, (125, 125, 125))
        self.text_name_rect = self.text.get_rect(center=(self.half_width, self.half_height + 40))
        self.button_back_menu = Button(300, 500, "REGRESAR")

    def draw(self, screen):
        # screen.blit(self.img, self.img_rect)
        screen.blit(self.text, self.text_rect)
        screen.blit(self.text_name, self.text_name_rect)
        self.button_back_menu.draw(screen)

    def update(self):
        self.button_back_menu.update()

    def verify_pressed(self):
        if self.button_back_menu.pressed:
            return 'Clicked'
        return 'Not Clicked'
