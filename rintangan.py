import pygame

# berfungsi unutuk mengatur tampilan obtacle dimana obtacle akan ditampilkan secara random dari 9 asset yang ada
class Rintang(pygame.sprite.Sprite):
    def __init__(self, index):
        super().__init__()
        obstacle_1 = pygame.image.load('Assets\Rintangan\bawang.jpg').convert_alpha()
        obstacle_2 = pygame.image.load('').convert_alpha()

        self.obstacle_list = [obstacle_1, obstacle_2]

        self.obstacle_index = index
        self.image = self.obstacle_list[self.obstacle_index]
        self.rect = self.image.get_rect(bottomright = (1700, 680))

    
    def mask(self):
        for i in self.obstacle_list:
            pygame.mask.from_surface(i)

    def random_obstacle(self):
        self.image = self.obstacle_list[self.obstacle_index]

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

    def update(self):
        self.mask()
        self.random_obstacle()
        self.destroy()
        self.rect.x -= 10 