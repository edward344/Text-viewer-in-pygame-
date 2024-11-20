import pygame
import data
import widgets

class File_menu:
    def __init__(self,screen):
        self.screen_height = screen.get_height()
        self.file_list = data.fetchall()
        self.subdirectory = "text-files/"
        self.open_button_list = []
        for index,row in enumerate(self.file_list):
            button = widgets.Button("open",400,80 + index * 60)
            self.open_button_list.append(button)
        self.label_list = []
        # Create a title with a font
        title_font = pygame.font.Font("Roboto-Regular.ttf",32)
        label_font = pygame.font.Font("Roboto-Regular.ttf",20)
        title_label = widgets.Label("height:" + str(screen.get_width()),title_font)
       # widgets.set_midpoint(screen,title_label.rect)
        title_label.set_initial_top(title_label.rect.top)
        # We append the title to the list
        self.label_list.append(title_label)
        for index,row in enumerate(self.file_list):
            id_number = str(row[0])
            filename = row[1]
            id_label = widgets.Label(id_number,label_font,20,90 + index * 60)
            filename_label = widgets.Label(filename,label_font,50,90 + index * 60)
            self.label_list.append(id_label)
            self.label_list.append(filename_label)

    def get_page_height(self):
        return self.open_button_list[-1].rect.bottom

    def check_button_click(self):
        for button in self.open_button_list:
            button.check_button_click()

    def mouse_released(self):
        for button in self.open_button_list:
            button.mouse_released()

    def update_position(self,height_diff):
        for button in self.open_button_list:
            button.rect.top = button.initial_top - height_diff
        for label in self.label_list:
            label.rect.top = label.initial_top - height_diff

    def get_filename(self):
        filename = ""
        for index,button in enumerate(self.open_button_list):
            if button.check_click():
                filename = self.subdirectory + self.file_list[index][1]
        return filename

    def display_frame(self,screen):
        for label in self.label_list:
            if label.rect.bottom > 0 and label.rect.top < self.screen_height:
                label.draw(screen)
        for button in self.open_button_list:
            if button.rect.bottom > 0 and button.rect.top < self.screen_height:
                button.draw(screen)
