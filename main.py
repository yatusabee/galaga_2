import pygame
from source.screen.screenGame import ScreenGame
from source.screen.screenResult import ScreenResult
from source.utils.menu import Menu
from source.utils.difficulty_selector import DifficultySelector
# init:
pygame.init()  # <--- recrear el contenido de pantalla
screen = pygame.display.set_mode((800, 600))  # <--- crear una pantalla 800 x 600
pygame.display.set_caption("Galaga Refactorized")  # título

sg = ScreenGame(screen)
menu = Menu(screen) # objeto de la clase menu
ds = DifficultySelector(screen)
sr = None
show_finish = True
show_menu = True # bool que indica si debo mostrar el menu o no
show_difficulty_selector = False
val = '' # tenga un valor al inicio

while True:
    sg.clock.tick(25)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sg.set_finished(True)
    sg.screen.fill((0, 0, 0))  # pintar el fondo 0,0,0
    if show_menu: # si esto es verdadero
        menu.update() # update de menu
        menu.draw() # draw de menu
        menu.events() # detectar si hubo algun click
        if menu.get_menu_finished() or show_difficulty_selector == True: # si hemos hecho click en el boton
            show_menu = False # false
            show_difficulty_selector = True
    elif show_difficulty_selector:
        ds.update()
        ds.draw()
        if ds.events() is not None:
            val = ds.events() # el valor de VAL se modifica
            print(val)
            sg.change_difficulty_game(val)
            show_difficulty_selector = False
    else:
        if sg.player.is_alive():
            sg.bg.update(sg.screen)
            sg.playGame()
        if not sg.player.is_alive() and show_finish == True:
            sg.set_finished(True)
            show_finish = False
            sr = ScreenResult(800, 600, False, score=sg.get_score())
        if sg.get_score() == 10:
            sr = ScreenResult(800, 600, True, score=sg.get_score())
            sg.set_finished(True)
            if val == 'hard':
                ds.show_very_hard_button() # puedo mostrar el caso de muy dificil
            # show_finish = False
        if not show_finish:
            sr.update()
            sr.draw(screen) # ganar o perder
            if sr.verify_pressed() != 'Not Clicked':
                sg.reset_game()
                sg.set_finished(False, 3)
                sg.reset_score()
                show_finish = True
                show_menu = True
                show_difficulty_selector = False
    pygame.display.update()
