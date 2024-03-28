# Paramètre fenêtre :
WINDOW_WIDTH = 1300 #1500
WINDOW_HEIGHT = 700 #750
Couleur = (17, 139, 86)
TourParSeconde = 60#120

# Paramètre Menu :
LongueurMenu = 330
LargeurMenu = 100
MarginMenu = 15
MarginButton = 10


# Image Menu
ImageSuprimerDesactiver = '../Image Simulateur/Menu Image/trash vide.png'
ImageSuprimerActiver = '../Image Simulateur/Menu Image/trash.png'
ImageTempsNormal = '../Image Simulateur/Menu Image/play.png'
ImageTempsRalentie = '../Image Simulateur/Menu Image/angle-right.png'
ImageTempsArrete = '../Image Simulateur/Menu Image/pause.png'
ImageRienAjouter = '../Image Simulateur/Menu Image/cross.png'
# Nombre entitées:
NombreHomme = 50
NombreFemme = 100
NombreArbre = 25
NombreOurs = 0

# Paramètre arbre:
ImageArbre = '../Image Simulateur/tree.png'
ImageArbreAvecPomme = '../Image Simulateur/apple-tree.png'
TailleArbre = (35, 35)
FrequenceApparitionPomme = 650
Nouriture = 1000


# Paramètre Humain
VieHumains = 200
NouritureDepart = 1000
QuantiteMaximalNouriture = 2500
IntervalleVitesseHumain = (1,5)
IntervalleVisionHumain = (100, 1000)
IntervalleAgeMortHumain = (1000, 15000)
EcartVision = 500
EcartVitesse = 5
TailleHumain = (30, 30)
DegatHumain = 8
TempsAdulte = (500, 0)
FormulePerteNouriture = 'self.speed*1.25 + (self.vision/75)'


# Paramètre Homme:
ImageHomme = '../Image Simulateur/man.png'

# Paramètre Femme:
ImageFemme = '../Image Simulateur/female.png'
TempsGestation = 120 #120

# Paramètre ours:
ImageOurs = '../Image Simulateur/bear.png'
TailleOurs = (40,40)
VieOurs = 800
IntervalleVitesseOurs = (1,8)
IntervalleVisionOurs = (25, 150)
DistanceAttaqueOurs = 10
DegatsOurs = 100



mapvide = [533, 546, 565, 579, 602, 622, 623, 645, 660, 663, 673, 675, 684, 717, 734, 744, 746, 750, 751, 763, 779, 799, 864, 867, 876, 891, 893, 922, 924, 926, 929, 933, 979, 986]
mappresquevide = [612]

"""
mapvide.sort()
print(mapvide)"""