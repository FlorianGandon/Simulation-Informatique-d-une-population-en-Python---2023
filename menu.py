import pygame
from settings import *
from time import sleep


class Menu:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        # menu area
        Position = (WINDOW_WIDTH-LongueurMenu-MarginMenu,
                    WINDOW_HEIGHT-LargeurMenu-MarginMenu)
        self.ZoneMenu = pygame.Rect(Position, (LongueurMenu, LargeurMenu))

        # Bouton Menu
        self.RectBoutonAjouter = pygame.Rect(self.ZoneMenu.topleft, (LargeurMenu, LargeurMenu))
        self.RectBoutonSuprimer = pygame.Rect((self.ZoneMenu.topleft[0]+LargeurMenu+MarginButton, self.ZoneMenu.topleft[1]), (LargeurMenu, LargeurMenu))
        self.RectBoutonTemps = pygame.Rect((self.ZoneMenu.topleft[0]+int(LargeurMenu*2+MarginButton*2), self.ZoneMenu.topleft[1]), (LargeurMenu, LargeurMenu))


        self.BoutonAjouter = BoutonMEtat(self.ZoneMenu.topleft, (LargeurMenu, LargeurMenu), (0,4), ("#ffffff", '#000000', '#000000', '#000000', '#000000'))
        self.BoutonSuprimer = BoutonMEtat((self.ZoneMenu.topleft[0]+LargeurMenu+MarginButton, self.ZoneMenu.topleft[1]), (LargeurMenu, LargeurMenu), (0,1), ("#ffffff", '#000000'))
        self.BoutonTemps = BoutonMEtat((self.ZoneMenu.topleft[0]+int(LargeurMenu*2+MarginButton*2), self.ZoneMenu.topleft[1]), (LargeurMenu, LargeurMenu))

    def draw_all(self, screen):
        self.BoutonTemps.draw(screen)
        self.BoutonAjouter.draw(screen)
        self.BoutonSuprimer.draw(screen)

    def update(self):
        self.BoutonTemps.check_click()
        self.BoutonAjouter.check_click()
        self.BoutonSuprimer.check_click()


class BoutonMEtat(pygame.sprite.Sprite):
    def __init__(self, position, taille, Borne=(0,2), Etats=('#ffffff', '#000000', '#7f7f7f')):
        self.Bouton = pygame.Rect(position, taille)
        self.Image = pygame.Surface(taille)
        self.Couleur = Etats[0]
        self.Borne = Borne
        self.Active = Borne[0]
        self.Etat = Etats
        self.t = False
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.Bouton.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.t = True
            else:
                if self.t:
                    self.t = False
                    if self.Active < self.Borne[1]:
                        self.Active += 1
                        self.Couleur = self.Etat[self.Active]
                    elif self.Active == self.Borne[1]:
                        self.Active = 0
                        self.Couleur = self.Etat[self.Active]

    def draw(self, screen):
        """
        self.Image.fill(self.Couleur)
        surf = 'tt.png'
        rect = surf.get_rect(center=(self.Bouton.width /2, self.Bouton.height / 2))
        self.Image.blit(surf, rect)"""
        pygame.draw.rect(screen, self.Couleur, self.Bouton, border_radius=12)

    def disable(self):
        self.Couleur = '#000000'
        self.Active = False

