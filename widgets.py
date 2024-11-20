import pygame
from colors import *

def set_midpoint(screen,rect):
    width,height = screen.get_size()
    rect.x = (width / 2) - (rect.width / 2)
    rect.y = height * .05

# Create a Label class
class Label:
    def __init__(self,text,font,x=50,y=50):
        self.text = text
        self.text_surface = font.render(self.text,True,BLACK)
        self.rect = pygame.Rect(x,y,self.text_surface.get_width(),self.text_surface.get_height())
        self.initial_top = self.rect.top

    def set_initial_top(self,top):
        self.initial_top = top

    def draw(self,screen):
        screen.blit(self.text_surface,self.rect)

# Create a class for printing text on the screen
class Printer:
    def __init__(self,size,color):
        self.font = pygame.font.Font("Roboto-Regular.ttf",size)
        self.color = color

    def print_text(self,screen,text,x,y):
        text_surface = self.font.render(text,True,self.color)
        screen.blit(text_surface,(x,y))

# Create a Button class
class Button:
    def __init__(self,text,x,y):
        self.font = pygame.font.Font("Kenney Future.ttf",20)
        self.text_surface = self.font.render(text,True,BLACK)
        image1 = pygame.image.load("button_rectangle_gloss.png")
        image2 = pygame.image.load("button_rectangle_border.png")
        # scale the images:
        width,height = image1.get_size()
        self.button_image1 = pygame.transform.scale(image1,(width * .7,height * .7))
        width,height = image2.get_size()
        self.button_image2 = pygame.transform.scale(image2,(width * .7,height * .7))
        self.click = False
        self.rect = pygame.Rect(x,y,self.button_image1.get_width(),self.button_image1.get_height())
        self.initial_top = self.rect.top

    def check_button_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.click = True

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            return True
        else:
            return False

    def mouse_released(self):
        self.click = False

    def draw(self,screen):
        if self.click:
            screen.blit(self.button_image2,self.rect)
        else:
            screen.blit(self.button_image1,self.rect)
        # Getting the width and height of the text
        text_width,text_height = self.text_surface.get_size()
        posX = self.rect.left + (self.rect.width / 2) - (text_width / 2)
        posY = self.rect.top + (self.rect.height / 2) - (text_height / 2)
        # print the text
        screen.blit(self.text_surface,(posX,posY))
