from source.utils.ui import Button


class DifficultySelector:
    def __init__(self, screen, show_very_hard=False):
        self.button_easy = Button(300, 100, "FACIL")
        self.button_medium = Button(300, 180, "MEDIO")
        self.button_hard = Button(300, 260, "DIFICIL")
        self.screen = screen
        self.show_very_hard = show_very_hard
        if self.show_very_hard:
            self.button_very_hard = Button(300, 340, "MUY DIFICIL")

    def show_very_hard_button(self):
        self.show_very_hard = True
        if self.show_very_hard:
            self.button_very_hard = Button(300, 340, "MUY DIFICIL")

    def events(self):
        '''
        :return: str
        '''
        if self.button_easy.clicked:
            return 'easy'
        elif self.button_medium.clicked:
            return 'medium'
        elif self.button_hard.clicked:
            return 'hard'
        if self.show_very_hard:
            if self.button_very_hard.clicked:
                return 'very hard'

    def update(self):
        self.button_easy.update()
        self.button_medium.update()
        self.button_hard.update()
        if self.show_very_hard:
            self.button_very_hard.update()

    def draw(self):
        self.button_easy.draw(self.screen)
        self.button_medium.draw(self.screen)
        self.button_hard.draw(self.screen)
        if self.show_very_hard:
            self.button_very_hard.draw(self.screen)


