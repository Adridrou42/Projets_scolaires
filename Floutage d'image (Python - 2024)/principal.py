
#floutage image

import pygame, sys
from pygame.locals import *

import gestion

#Dimension de la fenêtre 500 x 400
WIDTH = 600
HEIGHT = 558
action = 0
taille = 50
flou = 5
background = (0,0,0)

#=========================================================================
#le programme principal
#création de la fenêtre

pygame.init()
rafraichissement = pygame.time.Clock()
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("PROJET ANONYMOUS")
image_original= gestion.chargement_image("personnages.png")


while True:
    window.fill(background)
    gestion.affiche_image(window,image_original,0,0)
    souris = pygame.mouse.get_pos()
    if action == 1:
        gestion.floutage(image_original,souris[0]-taille//2,souris[1]-taille//2,taille,taille,flou)
    if action == 2:
       image_original= gestion.chargement_image("personnages.png")
       
    pygame.draw.rect(window,(225,0,0),pygame.Rect(souris[0]-taille//2,souris[1]-taille//2,taille,taille),2)
    my_font = pygame.font.Font(None, 15)
    text_surface = my_font.render('Floutage: ' + str(flou), True, (0, 0, 255))  # Texte en rouge
    window.blit(text_surface, (souris[0]-taille//2,souris[1]-taille//2-10))  # Positionnez le texte à (100, 100)


    for evenement in pygame.event.get():

        if evenement.type == QUIT:  #croix rouge
            pygame.quit()
            sys.exit()

        if evenement.type == pygame.MOUSEBUTTONDOWN:
            if evenement.button == 1: # clic gauche 
                action = 1

        if evenement.type == pygame.MOUSEBUTTONUP:
            if evenement.button == 1: # clic gauche 
                action = 0

        if evenement.type == pygame.KEYDOWN:
            if evenement.key == K_SPACE:
                action = 2
            if evenement.key == K_UP:
                flou += 1
            if evenement.key == K_DOWN and flou > 1:
                flou -= 1
            if evenement.key == K_RIGHT:
                taille += 5
            if evenement.key == K_LEFT and taille > 5:
                taille -= 5


    pygame.display.update()
    rafraichissement.tick(60)  # framerate




