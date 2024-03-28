import pygame, sys
from homme import Homme, Femme
from arbre import Arbre
from menu import Menu
from ours import Ours
from settings import *
import map

class Monde:
    def __init__(self):
        map.creerMap()
        self.Fenetre = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Simulateur')
        self.EnCours = True
        self.Horloge = pygame.time.Clock()
        self.menu = Menu()
        self.AfficherMenu = False
        
        self.ListElement = pygame.sprite.Group()
        
        self.ClickActif = False
        
        self.tours = 0
        
        # Humains
        self.Humains = pygame.sprite.Group()
        for nombre in range(NombreHomme):
            self.NouveauHomme()
        
        for nombre in range(NombreFemme):
            self.NouvelleFemme()
            
        # Arbres
        self.Arbres = pygame.sprite.Group()
        for nombre in range(NombreArbre):
            self.NouveauArbre()
        # Ours
        self.ListeOurs = pygame.sprite.Group()
        for nombre in range(NombreOurs):
            self.NouveauOurs()
    def NouveauOurs(self, co=None):
        NouveauOurs = Ours(co)
        self.ListeOurs.add(NouveauOurs)
        self.ListElement.add(NouveauOurs)
    
    def NouveauArbre(self, co = None):
        NouveauArbre = Arbre(co)
        self.Arbres.add(NouveauArbre)
        self.ListElement.add(NouveauArbre)
    
    def NouveauHomme(self):
        NouvauIndividu = Homme()
        NouvauIndividu.Nouriture = 6000
        self.Humains.add(NouvauIndividu)
        self.ListElement.add(NouvauIndividu)
    
    def NouvelleFemme(self):
        NouvauIndividu = Femme()
        NouvauIndividu.Nouriture = 6000
        self.Humains.add(NouvauIndividu)
        self.ListElement.add(NouvauIndividu)
    def hangling_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("----------------")
                """
                for Humain in self.Humains:
                    Humain.info()
                    Humain.kill()"""
                sys.exit()
                self.EnCours = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    self.AfficherMenu = not self.AfficherMenu
        
        for Humain in self.Humains:
            Humain.check_click(self.menu.BoutonSuprimer.Active==1)
        
        for Ours in self.ListeOurs:
            Ours.check_click(self.menu.BoutonSuprimer.Active==1)
                
        for Arbre in self.Arbres:
            Arbre.check_click(self.menu.BoutonSuprimer.Active==1)
        
        if not self.menu.BoutonAjouter.Active ==0:
            NouvauOurs = None
            mouse_pos = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:
                if not (self.menu.BoutonTemps.Bouton.collidepoint(mouse_pos) or self.menu.BoutonSuprimer.Bouton.collidepoint(mouse_pos) or self.menu.BoutonAjouter.Bouton.collidepoint(mouse_pos)):
                    self.ClickActif = True
            else:
                if self.ClickActif:
                    self.ClickActif = False
                    if self.menu.BoutonAjouter.Active == 1:
                        self.NouveauArbre(mouse_pos)
                    elif  self.menu.BoutonAjouter.Active == 2:
                        self.NouveauOurs(mouse_pos)
                    elif  self.menu.BoutonAjouter.Active == 3:
                        self.NouveauHomme()
                    elif  self.menu.BoutonAjouter.Active == 4:
                        self.NouvelleFemme()
        
    
    def update(self):
        
        if not self.menu.BoutonTemps.Active == 1:
            self.tours += 1
            for Humain in self.Humains:
                Humain.update(self.ListElement, self.Humains)
            
            for Ours in self.ListeOurs:
                Ours.update(self.Humains)
                
            for Arbre in self.Arbres:
                Arbre.modifier()
            
        if self.AfficherMenu:
            self.menu.update()
        
        
        
    def displayFenetre(self):
        ArrierePlan = pygame.image.load('noise.png')
        self.Fenetre.blit(ArrierePlan, (0,0))
        #self.Fenetre.fill(Couleur)
        
        for Arbre in self.Arbres:
            Arbre.draw(self.Fenetre)
        
        for Humain in self.Humains:
            Humain.draw(self.Fenetre)
        
        for Ours in self.ListeOurs:
            Ours.draw(self.Fenetre)
        
    def displayMenu(self):
        if self.AfficherMenu:
            self.menu.draw_all(self.Fenetre)
    def display(self):
        self.displayFenetre()
        self.displayMenu()
        pygame.display.flip()
    
    def fin(self):
        if len(self.Humains) == 0:
            print("fini, en :", self.tours, "tours.")
            self.EnCours = False
            pygame.quit()

    def run(self):
        while self.EnCours:
            self.hangling_event()
            self.update()
            self.display()
            self.fin()
            if self.menu.BoutonTemps.Active == 2:
                self.Horloge.tick(TourParSeconde/2)#30
            else:
                self.Horloge.tick(TourParSeconde)
                    

                    
pygame.init()



game = Monde()
game.run()
pygame.quit()
