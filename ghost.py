import pygame
from abc import ABC, abstractclassmethod

# Parrent class
class Player(pygame.sprite.Sprite, ABC):
    def __init__(self):
        super().__init__()

        self.gravity = 0
       

    @abstractclassmethod
    def masking(self):
        pass
            
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 680:
            self.gravity = -15
            self.player_index = 0
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 680:
            self.rect.bottom = 680
    
    @abstractclassmethod
    def animation_state(self):
        pass


    def update(self):
        self.masking()
        self.player_input()
        self.apply_gravity()
        self.animation_state()

# berfungsi unutk mengatur animasi player pada saat lompat atau berlari
class Kucing_1(Player):
    def __init__(self):
        super().__init__()
        player_walk1 = pygame.image.load('assets/Other/bird/Grim Reaper.png.jpg').convert_alpha()
        self.player_walk = [player_walk1]

        player_jump1 = pygame.image.load('assets/Other/bird/Grim Reaper.png.jpg').convert_alpha()
        
        self.player_jump = [player_jump1]
        self.player_index = 0

        self.image = self.player_walk[self.player_index]        
        self.rect = self.image.get_rect(midbottom = (300, 680))

    def masking(self):
        for masking1 in self.player_walk:
            pygame.mask.from_surface(masking1)
        for masking2 in self.player_jump:
            pygame.mask.from_surface(masking2)
        
    def animation_state(self):         
        if self.rect.bottom < 680:
            # jump
            self.player_index += 0.223
            if self.player_index >= len(self.player_jump):
                self.player_index = 0
            self.image = self.player_jump[int(self.player_index)]
        else:
            # walk
            self.player_index += 0.31
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]