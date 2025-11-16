import pygame, sys
from pygame.locals import *

#=========================================================================
# chargement de l'image à flouter

def chargement_image(chemin_image):
    image = pygame.image.load(chemin_image)
    mon_image = image.convert_alpha()
    return mon_image


#=========================================================================
# affichage de l'image dans la fenêtre pygame
def affiche_image(fenetre, mon_image, x,y):
    fenetre.blit(mon_image,(x,y))


#=========================================================================
# floute l'image par n*n pixels
def floutage(mon_image,position_x, position_y, largeur, hauteur,n=10): # floute l'image par n pixels
    
    n_hauteur= hauteur //n
    hauteur= n * n_hauteur # on recalcule les dimensions afin d'éviter des effets de bord
       
    n_largeur = largeur //n
    largeur= n* n_largeur
    
    dimensions=mon_image.get_size()  
    
    if (position_x >0) and (position_x + largeur < dimensions[0]) and (position_y >0) and (position_y + hauteur < dimensions[1]) :

        # autoriser à flouter

        hauteur_courante = position_y
        largeur_courante = position_x

        largeur_totale = position_x + largeur
        hauteur_totale = position_y + hauteur


        while hauteur_courante < hauteur_totale:  #balayage hauteur
            largeur_courante = position_x

            while largeur_courante < largeur_totale:
                couleur= [0,0,0]  # RVB

                for x in range(largeur_courante, largeur_courante + n):
                    for y in range(hauteur_courante, hauteur_courante + n):
                        color =tuple(mon_image.get_at((x,y)))
                        couleur[0] = couleur[0] + color[0]
                        couleur[1] = couleur[1] + color[1]
                        couleur[2] = couleur[2] + color[2]


                couleur[0] = couleur[0] //(n*n)
                couleur[1] = couleur[1] //(n*n)
                couleur[2] = couleur[2] //(n*n)

                for x in range(largeur_courante, largeur_courante + n):
                    for y in range(hauteur_courante, hauteur_courante + n):
                        mon_image.set_at((x, y), (couleur[0], couleur[1], couleur[2]))

                largeur_courante= largeur_courante + n


            hauteur_courante= hauteur_courante + n
            
        return mon_image

    else:
        return "out"



