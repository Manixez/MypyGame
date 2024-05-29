import pygame
from abc import ABC, abstractmethod
from dasar import *

# parrent class
class Button(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def button_display(self):
        pass
    
    @abstractmethod
    def action(self):
        pass

# berfungsi untuk memulai permainan
class Button_play(Button):
    def __init__(self):
        super().__init__()
        self.button = pygame.image.load('Assets/Tombol/mulai.png').convert_alpha()
        self.button = pygame.transform.scale(self.button,(100,50))
        self.x = 500
        self.y = 400
        self.rect = self.button.get_rect(center = (self.x, self.y))
        self.cond = True
    
    def button_display(self):
        screen.blit(self.button, self.rect)

    def action(self):
        pass    
    
    def update(self):
        self.action()

# berfungsi untuk menampilkan pause pada saat game dimulai
class Button_Pause(Button):
    def __init__(self):
        super().__init__()
        self.button = pygame.image.load('Assets/Tombol/pause.png').convert_alpha()
        self.button = pygame.transform.scale(self.button, (100,80))
        self.bg = pygame.image.load('Assets/Bg/Background2.jpg').convert_alpha()
        self.setting_message = font.render(f"Pause", False, ("#e6e7e7"))
        self.rect_board = self.bg.get_rect(center = (500, 350))
        self.setting_message_rect = self.setting_message.get_rect(center = (500, 200))
        self.x = 900
        self.y = 80
        self.rect = self.button.get_rect(topright = (self.x, self.y))
        self.cond = True
        self.jenis = "setting"
    
    def button_display(self):
        screen.blit(self.button, self.rect)

    def action(self, cond):
        return cond
    
    def display_board(self):
        screen.blit(self.bg, self.rect_board)
        screen.blit(self.setting_message, self.setting_message_rect)
        
    def update(self):
        self.action()

# berfungsi untuk menampilkan menu pilih tema pada homepage
class Button_Theme(Button):
    def __init__(self, number, x, y):
        super().__init__()
        self.button = pygame.image.load(f'Assets/Bg/Background{number + 1}.jpg').convert_alpha()
        self.button = pygame.transform.scale(self.button,(200, 110))
        self.x = x
        self.y = y
        self.rect = self.button.get_rect()
        self.rect.topleft = (x, y)
    
    def action(self):
        pass

    def button_display(self):
        screen.blit(self.button, self.rect)    

    def update(self):
        self.action()

# berfungsi untuk melanjutkan permainan pada saat permainan di pause
class Button_resume(Button):
    def __init__(self):
        super().__init__()
        self.button = pygame.image.load('Assets/Tombol/mulai.png').convert_alpha()
        self.button = pygame.transform.scale(self.button,(100,50))
        self.x = 500
        self.y = 300
        self.rect = self.button.get_rect(center = (self.x, self.y))
        self.cond = True
        self.jenis = "resume"
    
    def button_display(self):
        screen.blit(self.button, self.rect)

    def action(self):
        pass
        
    def update(self):
        self.action()

# berfungsi untuk kembali ke homepage
class Button_home(Button):
    def __init__(self):
        super().__init__()
        self.button = pygame.image.load('Assets/Tombol/home.png').convert_alpha()
        self.button_game_over = pygame.image.load('Assets/Tombol/game_end.png').convert_alpha()
        self.x = 700
        self.y = 450
        self.rect = self.button.get_rect(center = (self.x, self.y))
        self.rect_game_over = self.button.get_rect(center = (500, 410))
        self.cond = True
        self.jenis = "home"
    
    def button_display(self):
        screen.blit(self.button, self.rect)
    
    def button_display_game_over(self):
        screen.blit(self.button_game_over, self.rect_game_over)

    def action(self):
        pass
        
    def update(self):
        self.action()
        