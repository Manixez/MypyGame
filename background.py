import pygame
from dasar import *

class Bg():
    def __init__(self):
        self.logo_surf = pygame.image.load('')
        self.logo_rect = self.logo_surf.get_rect(center = (800, 255))


    def display_logo(self):
        layar.blit(self.logo_surf,self.logo_rect)
    

# untuk menampilkan tema 1
class Bg_1(Bg):
    def __init__(self):
        super().__init__()
        self.sky_surface = pygame.image.load('Assets\Bg\Background1.jpg').convert_alpha()
        self.ground_surface = pygame.image.load('Assets\Bg\tanah1.png').convert_alpha()

    def display_bg(self):
        layar.blit(self.sky_surface, (0,0))
        layar.blit(self.ground_surface, (0,254))

# untuk menampilkan tema 2
class Bg_2(Bg):
    def __init__(self):
        super().__init__()
        self.sky_surface = pygame.image.load('Assets\Bg\Background2.jpg').convert_alpha()
        self.ground_surface = pygame.image.load('Assets\Bg\tanah1.png').convert_alpha()

    def display_bg(self):
        layar.blit(self.sky_surface, (0,0))
        layar.blit(self.ground_surface, (0,254))