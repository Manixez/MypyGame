from dasar import *

# melakukan perhitungan skor dan menampilkan skor pada saat game dimulai
class skor:
    def __init__(self,skor):
        self.__current_skor = skor
        self.__score_surf = font.render(f"score {self.__current_skor}", False, ("#404040"))
        self.__score_rect = self.__score_surf.get_rect(center = (800, 255))
    def display_score(self):
        layar.blit(self.__score_surf, self.__score_rect) 
        return self.__current_skor
    

    def update(self):
        self.display_score()