import pygame
from dasar import *

# melakukan perhitungan sesajen yang didapat dan menampilkan sesajen saat game akan mulai
class sesajen(pygame.sprite.Sprite):
    def __init__(self, sum, cn):
        super().__init__()

        sesajen = pygame.image.load('Assets\sajen\Sajen.jpg').convert_alpha()
        self.__sesajen_display = pygame.image.load('Assets\sajen\Sajen.jpg').convert_alpha()
        self.__sesajen_list = [sesajen]
        self.__sesajen_index = 0
        self.image = self.__sesajen_list[self.__sesajen_index]
        self.rect = self.image.get_rect(midbottom = (570, 150))
        self.__sesajen_display_rect = self.image.get_rect(center = (25, 25))
        self.__total_sesajen = sum
        self.__sesajen = sesajen.render(f"{cn}", False, ("#404040"))
        self.__sesajen_in_run = sesajen.render(f"{sum}", False, ("#404040"))
        self.__sesajen_rect = self.__sesajen.get_rect(topleft = (40, 15))
        

    def mask(self):
        for i in self.__sesajen_list:
            pygame.mask.from_surface(i)

    def animation_state(self):
            self.__sesajen_index += 0.1
            if self.__sesajen_index >= len(self.__sesajen_list):
                self.__sesajen_index = 0
            self.image = self.__sesajen_list[int(self.__sesajen_index)]
    
    def display_sesajen(self):
        layar.blit(self.__sesajen_display, self.__sesajen_display_rect)
        layar.blit(self._sesajen_, self.__koin_rect)
    
    def display_sesajen_in_run(self):
        layar.blit(self.__sesajen_display, self.__sesajen_display_rect)
        layar.blit(self.__sesajen_in_run, self.__sesajen_rect)

    def destroy(self):
        if self.rect.x <= -80:
            self.kill()

    def sesajen_return(self, cn):
        return self.__sesajen_koin + cn


    def update(self):
        self.mask()
        self.animation_state()
        self.rect.x -= 10 