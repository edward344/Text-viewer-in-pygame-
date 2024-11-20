import pygame
from colors import *

class Text:
    def __init__(self,text,screen):
        self.screen_width = screen.get_width() - 20 # 20 pixels is the width of the scrollbar
        self.screen_height = screen.get_height()
        self.word_list = text.split()
        self.font = pygame.font.Font("Roboto-Regular.ttf",20)
        self.word_surface_list = []

        text_width = 10
        text_height = 20
        for word in self.word_list:
            word_surface = Word(word,self.font,text_width,text_height)
            text_width = text_width + word_surface.get_width() + 10
            if text_width > self.screen_width:
                word_surface.rect.left = 10
                text_height = text_height + word_surface.get_height() + 10
                text_width = 10 + word_surface.get_width() + 10
                word_surface.rect.top = text_height
                word_surface.initial_top = text_height
            self.word_surface_list.append(word_surface)

    def get_page_height(self):
        last_word = self.word_surface_list[-1]
        return last_word.rect.bottom

    def update_position(self,height_diff):
        for word in self.word_surface_list:
            word.rect.top = word.initial_top - height_diff
            

    def display_frame(self,screen):
        for word in self.word_surface_list:
            if word.rect.bottom > 0 and word.rect.top < self.screen_height:
                word.draw(screen)


class Word:
    def __init__(self,text,font,x,y):
        self.text_surface = font.render(text,True,BLACK)
        width,height = self.text_surface.get_size()
        self.rect = pygame.Rect(x,y,width,height)
        self.initial_top = self.rect.top

    def get_width(self):
        return self.rect.width

    def get_height(self):
        return self.rect.height

    def draw(self,screen):
        screen.blit(self.text_surface,self.rect)
