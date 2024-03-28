import pygame
from random import randint
from settings import *
pygame.init()

class Arbre(pygame.sprite.Sprite):
    def __init__(self, coordonne=None):
        super().__init__()
        self.type = "Arbre"
        
        self.Image = pygame.image.load(ImageArbre)
        self.Image = pygame.transform.scale(self.Image, TailleArbre)
        self.Rect = self.Image.get_rect()
        if coordonne == None:
            self.Rect.x = randint(0, WINDOW_WIDTH-TailleArbre[0])
            self.Rect.y = randint(0, WINDOW_HEIGHT-TailleArbre[1])
        else:
            self.Rect.x = coordonne[0]-(TailleArbre[0]/2)
            self.Rect.y = coordonne[1]-TailleArbre[1]
        
        self.Pomme = False
        self.Active = False
    def draw(self, screen):
        screen.blit(self.Image, self.Rect)
    
    def modifier(self):
        if not self.Pomme:
            if randint(1, FrequenceApparitionPomme) == 1:
                self.Pomme = True
                self.Image = pygame.image.load(ImageArbreAvecPomme)
                self.Image = pygame.transform.scale(self.Image, TailleArbre)
    
    def co(self):
        return (self.Rect.x, self.Rect.y)
    
    def interaction(self):
        self.Pomme = False
        self.Image = pygame.image.load(ImageArbre)
        self.Image = pygame.transform.scale(self.Image, TailleArbre)

    def check_click(self, bool):
        mouse_pos = pygame.mouse.get_pos()
        if self.Rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.Active = True
            else:
                if self.Active:
                    self.Active = False
                    if bool:
                        self.kill()
                    else:
                        self.co()
