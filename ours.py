import pygame
from random import randint
from math import sqrt
from settings import *

pygame.init()

def distance(x_1, y_1, x_2, y_2):
    return sqrt((x_2-x_1)**2+(y_2-y_1)**2)

class Ours(pygame.sprite.Sprite):
    def __init__(self, coordonne=None):
        super().__init__()
        self.type = 'Ours'
        self.vie = VieOurs
        
        self.age = 0
        self.speed = randint(IntervalleVitesseOurs[0],IntervalleVitesseOurs[1])
        self.vision = randint(IntervalleVisionOurs[0], IntervalleVisionOurs[1])
        
        self.Image = pygame.image.load(ImageOurs)
        self.Image = pygame.transform.scale(self.Image, TailleOurs)
        
        self.Rect = self.Image.get_rect()
        if coordonne == None:
            self.Rect.x = randint(0, WINDOW_WIDTH-TailleOurs[0])
            self.Rect.y = randint(0, WINDOW_HEIGHT-TailleOurs[1])
        else:
            self.Rect.x = coordonne[0]-(TailleOurs[0]/2)
            self.Rect.y = coordonne[1]-TailleOurs[1]
        
        self.objectif = (randint(0, WINDOW_WIDTH-TailleOurs[0]),randint(0, WINDOW_HEIGHT-TailleOurs[1]))
        self.Active = False
    def draw(self, screen):
        screen.blit(self.Image, self.Rect)

    def co(self):
        return (self.Rect.x, self.Rect.y)
    
    def ChoisirObjectif(self, ListeHumains):
        NouvelleList = []
        for Humain in ListeHumains:
            NouvelleList.append((distance(self.Rect.x, self.Rect.y, Humain.co()[0], Humain.co()[1]), Humain.co(), Humain))
        NouvelleList.sort(key=lambda x: x[0])
        if len(ListeHumains) > 0:
            if NouvelleList[0][0] <= DistanceAttaqueOurs:
                Humain.hurt(DegatsOurs)
                if len(ListeHumains) > 1:
                    if NouvelleList[1][0] <= self.vision:
                        self.objectif = ( NouvelleList[1][1][0], NouvelleList[1][1][1])
                    else:
                        self.objectif = (randint(0, WINDOW_WIDTH-TailleOurs[0]),randint(0, WINDOW_HEIGHT-TailleOurs[1]))
            elif NouvelleList[0][0] <= self.vision:
                self.objectif = ( NouvelleList[0][1][0], NouvelleList[0][1][1])
            else:
                self.objectif = (randint(0, WINDOW_WIDTH-TailleOurs[0]),randint(0, WINDOW_HEIGHT-TailleOurs[1]))
    
    def avancer(self):
        for v in range(self.speed):
            if self.Rect.x > self.objectif[0]:
                self.Rect.x -= 1
            elif self.Rect.x < self.objectif[0]:
                self.Rect.x += 1
            if self.Rect.y > self.objectif[1]:
                self.Rect.y -= 1
            elif self.Rect.y < self.objectif[1]:
                self.Rect.y += 1
    
    def update(self, ListeHumains):
        self.ChoisirObjectif(ListeHumains)
        self.avancer()
    
    def hurt(self, degat):
        self.vie -= degat
        if self.vie <= 0:
            self.kill()
    
    def info(self):
        print(self.type, ', vie : ', self.vie, ", vision : ", self.speed, ", vie : ", self.vie)
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
                        self.info()