import pygame
from colors import *

class Scrollbar:
    def __init__(self,screen,content):
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.content = content
        self.page_width = screen.get_width()
        self.page_height = content.get_page_height()
        self.scrollbar_bg_rect = pygame.Rect(self.screen_width - 20,0,20,self.screen_height)
        if self.page_height > self.screen_height:
            divisor = self.page_height / self.screen_height
            self.scrollbar_rect = pygame.Rect(self.screen_width -20,0,20,int(self.screen_height / divisor))
        else:
            self.scrollbar_rect = pygame.Rect(self.screen_width -20,0,20,self.screen_height)
        self.mouse_over = False
        self.scrollbar_diff = 0

    def check_mouse(self):
        x,y = pygame.mouse.get_pos()
        if self.scrollbar_rect.collidepoint((x,y)):
            self.mouse_over = True
            self.scrollbar_diff = y - self.scrollbar_rect.top

    def check_mouse_released(self):
        self.mouse_over = False

    def update(self):
        if self.mouse_over:
            x,y = pygame.mouse.get_pos()
            self.scrollbar_rect.top = y - self.scrollbar_diff

        if self.scrollbar_rect.top < 0:
            self.scrollbar_rect.top = 0
        elif self.scrollbar_rect.bottom > self.screen_height:
            self.scrollbar_rect.bottom = self.screen_height

        quotient = self.page_height / self.screen_height
        height_diff = int(self.scrollbar_rect.top * quotient)

        self.content.update_position(height_diff)

    def display_frame(self,screen):
        self.content.display_frame(screen)
        pygame.draw.rect(screen,LIGHT_GRAY,self.scrollbar_bg_rect)
        pygame.draw.rect(screen,GRAY,self.scrollbar_rect)
