import pygame
from random import randint
from math import sqrt
from settings import *

pygame.init()

# calculer la distance entre deux points
def distance(x_1, y_1, x_2, y_2):
    return sqrt((x_2-x_1)**2+(y_2-y_1)**2)

class Humain(pygame.sprite.Sprite):
    def __init__(self, apparence, sexe, coordonne = None, vision=None, speed=None):
        super().__init__()
        # ici ces deux lines ne sont pas très utiles 
        self.ecart_vision = EcartVision
        self.ecart_speed = EcartVitesse


        self.type = sexe
        
        self.vie = VieHumains
        
        #paramètre Homme :
        self.age = 0
        self.Nouriture = NouritureDepart
        self.maxNouriture = QuantiteMaximalNouriture

        # on calcule des paramètres selon si on en donne ou pas
        if vision == None:
            self.vision = randint(IntervalleVisionHumain[0], IntervalleVisionHumain[1])
        else:
            self.vision = vision-randint(-self.ecart_vision, self.ecart_vision)
            while self.vision <= 0:
                self.vision = vision-randint(-self.ecart_vision, self.ecart_vision)

        if speed == None:
            self.speed = randint(IntervalleVitesseHumain[0], IntervalleVitesseHumain[1])
        else:
            self.speed = speed-randint(-self.ecart_speed, self.ecart_speed)
            while self.speed <= 0:
                self.speed = speed-randint(-self.ecart_speed, self.ecart_speed)
        self.temps = randint(IntervalleAgeMortHumain[0], IntervalleAgeMortHumain[1])
        
        # l' "humain" peut errer donc il ne vise rien d'important
        self.ViseImportant = False
        # charger l'image
        self.Image = pygame.image.load(apparence)
        self.Image = pygame.transform.scale(self.Image, TailleHumain)
        
        self.Rect = self.Image.get_rect()
        # on calcule des paramètres (position du joueur) selon si on en donne ou pas
        if coordonne == None:
            self.Rect.x = (WINDOW_WIDTH-TailleHumain[0])/2
            self.Rect.y = (WINDOW_HEIGHT-TailleHumain[1])/2
        else:
            self.Rect.x = coordonne[0]
            self.Rect.y = coordonne[1]
        
        # self object sont les coordonnées où il vas aller
        self.objectif = [randint(0, WINDOW_WIDTH-TailleHumain[0]), randint(0, WINDOW_HEIGHT-TailleHumain[1])]
        self.Active = False
    
    def draw(self, screen):
        screen.blit(self.Image, self.Rect)
    
    def co(self):
        return (self.Rect.x, self.Rect.y)
    
    # c'est l'équivalent du toString sans en avoir connaissances
    def info(self):
        print(self.type, ", vision : ", self.vision, ", vitesse : ",self.speed, ", age : ", self.age, ", vie : ", self.vie, ", nouriture : ", self.Nouriture, ", perte nouriture : ", eval(FormulePerteNouriture))
    
    # oula ... l'idée est de savoir ou vas l' "humain", de façon non-optimiser
    def choisirObjectif(self, ListeElement):
        # ListeElement regroupe tout les éléments (humains, arbres, ...) sur la fenêtre
        # newList vas regrouper tout les éléments intéressants pour cette personne
        newList = []
        for Element in ListeElement:
            # on ajoute tout les arbres qui contiennent des pommes si la personnes peut manger
            if Element.type == "Arbre" and self.Nouriture + Nouriture <= self.maxNouriture:
                if Element.Pomme:
                    newList.append((distance(self.Rect.x, self.Rect.y, Element.co()[0], Element.co()[1]), Element.co(), Element))
            # on ajoute tout les personnes qui peuvent enfanter avec cette personnes
            elif Element.type != self.type and not Element.type == "Arbre" and not Element.type == "Ours":
                if self.type == 'femme':
                    if self.gestation == -1:
                        if Element.Dispo():
                            newList.append((distance(self.Rect.x, self.Rect.y, Element.co()[0], Element.co()[1]), Element.co(), Element))
                else:
                    if Element.Dispo():
                        newList.append((distance(self.Rect.x, self.Rect.y, Element.co()[0], Element.co()[1]), Element.co(), Element))
            # si un ours est trop proche on l'attaque
            if Element.type == 'Ours' and distance(self.Rect.x, self.Rect.y, Element.co()[0], Element.co()[1]) < 50:
                Element.hurt(DegatHumain)
        # oui, on trie la liste en fonction de la distance
        newList.sort(key=lambda x: x[0])

        
        if len(newList)>0 and newList[0][0] <= self.vision:
            self.objectif = [newList[0][1][0], newList[0][1][1]]
            self.ViseImportant = True
            if int(newList[0][0]) <= 10:
                newList[0][2].interaction()
                if newList[0][2].type == 'Arbre':
                    self.Nouriture += Nouriture
        elif len(newList) == 0 and self.ViseImportant:
            self.objectif = [randint(0, WINDOW_WIDTH-TailleHumain[0]), randint(0, WINDOW_HEIGHT-TailleHumain[1])]
            self.ViseImportant = False
            if self.Rect.x == self.objectif[0] and self.Rect.y == self.objectif[1]:
                self.objectif = [randint(0, WINDOW_WIDTH-TailleHumain[0]), randint(0, WINDOW_HEIGHT-TailleHumain[1])]
        elif self.Rect.x == self.objectif[0] and self.Rect.y == self.objectif[1]:
                self.objectif = [randint(0, WINDOW_WIDTH-TailleHumain[0]), randint(0, WINDOW_HEIGHT-TailleHumain[1])]

    
    
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
    
    def ChangerValeurs(self, ListeElement, ListeHumain):
        self.age += 1
        self.Nouriture -= eval(FormulePerteNouriture)
        if self.age >= self.temps:
            #self.info()
            self.kill()
            #print("mort par age")
        if TempsAdulte[0] <= self.age <= self.temps-TempsAdulte[1] and not self.dispo:
            if self.type == 'femme':
                if self.gestation == -1:
                    self.dispo = True
                else:
                    self.gestationEnCours(ListeElement, ListeHumain)
                    self.dispo = False
            else:
                self.dispo = True
        elif TempsAdulte[0] >= self.age or self.age >= self.temps-TempsAdulte[1]:
            self.dispo = False
        if self.Nouriture <= 0:
            if len(ListeHumain) == 1:
                self.info()
            self.kill()
            #print("mort par nourriture")
        
        if self.vie <= 0:
            self.kill()
        
    def update(self, ListeElement, ListeHumain):
        self.choisirObjectif(ListeElement)
        self.avancer()
        self.ChangerValeurs(ListeElement, ListeHumain)
    
    def hurt(self, degat):
        self.vie -= degat



class Homme(Humain):
    def __init__(self, coordonne = None, vision=None, speed = None):
        Humain.__init__(self,ImageHomme, 'homme', coordonne, vision, speed)
        self.dispo = False
        
    def Dispo(self):
        return self.dispo
    
    def interaction(self):
        pass

class Femme(Humain):
    def __init__(self, coordonne = None, vision=None, speed = None):
        Humain.__init__(self, ImageFemme, 'femme', coordonne, vision, speed)
        
        self.dispo = False
        self.gestation = -1
    def Dispo(self):
        return self.dispo
    
    def interaction(self):
        self.dispo = False
        self.gestation = TempsGestation
    
    def gestationEnCours(self, ListeElement, ListeHumain, vision=None):
        self.gestation -= 1
        if self.gestation == 0:
            choix2 = randint(1,600)
            self.gestation = -1
            nbEnfant = 1
            if choix2 == 1 : nbEnfant = 3
            elif choix2 <= 7 : nbEnfant = 2
            for k in range(nbEnfant):
                choix = randint(0,10)
                if choix == 0:
                    NewMan = Homme((self.Rect.x, self.Rect.y), self.vision, self.speed)#, self.vision
                    ListeHumain.add(NewMan)
                    ListeElement.add(NewMan)
                else:
                    NewWoman = Femme((self.Rect.x, self.Rect.y), self.vision , self.speed)#, self.speed
                    ListeHumain.add(NewWoman)
                    ListeElement.add(NewWoman)
