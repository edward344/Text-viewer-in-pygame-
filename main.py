import pygame
from text import Text
from scrollbar_widget import Scrollbar
from colors import *
from file_menu import File_menu

# pygame setup
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Text Viewer")
clock = pygame.time.Clock()
running = True

show_files = True
file_menu = File_menu(screen)
text = Text("empty text",screen)
text_scrollbar = Scrollbar(screen,text)
file_menu_scrollbar = Scrollbar(screen,file_menu)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if show_files:
                # Get the filename if the user clicked a button
                filename = file_menu.get_filename()
                if filename:
                    with open(filename,"r") as file:
                        content = file.read()
                    # Open the text file
                    text = Text(content,screen)
                    text_scrollbar = Scrollbar(screen,text)
                    show_files = False
                else:
                    file_menu.check_button_click()
                    file_menu_scrollbar.check_mouse()
            else:
                text_scrollbar.check_mouse()
        elif event.type == pygame.MOUSEBUTTONUP:
            if show_files:
                file_menu.mouse_released()
                file_menu_scrollbar.check_mouse_released()
            else:
                text_scrollbar.check_mouse_released()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                show_files = True
                file_menu.mouse_released()

    if show_files:
        file_menu_scrollbar.update()
    else:
        text_scrollbar.update()
    # fill the screen with a color to wipe away anything from last frame
    screen.fill(WHITE)

    # RENDER YOUR GAME HERE
    if show_files:
        file_menu_scrollbar.display_frame(screen)
    else:
        text_scrollbar.display_frame(screen)
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
