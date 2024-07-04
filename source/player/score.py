import pygame


class Score:
    def __init__(self):
        self.font = pygame.font.SysFont('Roboto', 25)
        self.score_text = None

    def draw(self, screen, sc):
         # sc = -1 # comentado por PJMG - 2/7/2024 - Hacía que el score se setee en -1
        self.score_text = self.font.render('Score: ' + str(sc), True, (255, 100, 100))
        screen.blit(self.score_text, (0, 560))
