import pygame
import sys
pygame.init()

from Player import player
from MainMenu import menu
from MapBuilder import MapMaker

def main():

    bgimage = pygame.transform.scale(pygame.image.load('Images/BG1.jpeg'), (1080, 720))

    gamerunning = True

    bg = pygame.display.set_mode((1080, 720))

    Map = MapMaker(bg)
    Player = player()
    Menu = menu(bg, Map)
    

    while gamerunning:

        bg.blit(bgimage, (0, 0))
        IsEditing = Menu.is_editing()

        Menu.menu_tabs()
        Menu.blit_edit_mode()
        Menu.redraw()

        Menu.check_for_spawn()
        Menu.check_for_delete()
        Menu.check_for_move()
        Menu.check_for_ruler()
        Menu.check_movement_select_enemy()
        Menu.check_cycle_movement_pattern()
        Menu.check_add_point()
        Menu.check_draw_points()

        Map.testprint()

        if IsEditing:
            Map.redraw_editing_enemies()
        

        Player.move(bg, IsEditing)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()




main()