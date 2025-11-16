#PONG pygame
import random
import pygame, sys
import time
from pygame.locals import *

pygame.init()
rafraichissement = pygame.time.Clock()

#Variables
WIDTH = 700
HEIGHT = 400
position = [350,200,-1,-1,1.5]    #position x; position y; coef x; coef y; vitesse
player = [200,0,0]     #position y; coef y; vitesse
player2 = [200,0,0]     #position y; coef y; vitesse
color_ball = [225,0,225]
score = [0,0]   #Score J1; Score J2
start = 2

#la fenêtre du jeu 700 x 400
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('PONG by Adrien - Loïs - Anelise')



#========================================================
def dessine_terrain(fenetre):
    BLACK = (0,0,0)
    WHITE = (255,255,255)

    fenetre.fill(BLACK)
    pygame.draw.line(fenetre, WHITE, (WIDTH//2,0), (WIDTH//2,HEIGHT), 1)
    pygame.draw.circle(fenetre, WHITE, [WIDTH//2, HEIGHT//2], 70, 1)

def quitter():
    pygame.draw.rect(window,(0,0,0),pygame.Rect(0,0,WIDTH,HEIGHT))
    my_font = pygame.font.Font("ressources/neon_pixel-7.ttf", 150)
    text_surface = my_font.render("AU REVOIR", True, (225, 225, 225))  # Texte en blanc
    window.blit(text_surface, (WIDTH//2-280, 100))  # Positionnez le texte
    pygame.display.update()
    rafraichissement.tick(60)  # framerate du jeu
    time.sleep(1)
    pygame.quit()
    sys.exit()


def ecran_titre(fenetre):
    while 1 > 0:
        pygame.draw.rect(window,(0,0,0),pygame.Rect(0,0,WIDTH,HEIGHT))
        my_font = pygame.font.Font("ressources/neon_pixel-7.ttf", 150)
        text_surface = my_font.render("PONG", True, (225, 225, 225))  # Texte en blanc
        fenetre.blit(text_surface, (WIDTH//2-120, 50))  # Positionnez le texte

        my_font = pygame.font.Font("ressources/clip.ttf", 24)
        text_surface = my_font.render("Adrien - Loïs - Anelise", True, (225, 225, 225))  # Texte en blanc
        fenetre.blit(text_surface, (WIDTH//2-120, 170))  # Positionnez le texte

        my_font = pygame.font.Font("ressources/clip.ttf", 15)
        text_surface = my_font.render("Appuyez sur ESPACE pour jouer", True, (225, 0, 225))  # Texte en violet
        fenetre.blit(text_surface, (WIDTH//2-110, 300))  # Positionnez le texte

        for event in pygame.event.get():    #Bouton ESPACE pressé
            if event.type == pygame.KEYDOWN: 
                if event.key == K_SPACE: return
            if event.type == QUIT:  #croix rouge
                quitter()
        pygame.display.update()
        rafraichissement.tick(60)  # framerate du jeu

def lancement_balle():
    alea = 0
    alea = random.randint(0,3)
    if alea == 0:
        return [350,-1,1]
    if alea == 1:
        return [350,-1,-1]
    if alea == 2:
        return [350,1,1]
    if alea == 3:
        return [350,1,-1]
    
 
#========================================================

#le programme principal du jeu
while True:

    if start == 2:  #Écran titre + reset
        ecran_titre(window)
        score = [0,0]
        start = 1
    dessine_terrain(window)

    if start == 1:  #Lancement de la balle
        start = lancement_balle()
        position[0] = start[0]; position[1] = 200; position[2] = start[1]; position[3] = start[2]; position[4] = 1.5
        color_ball = [225, 0, 225]
        start = 0

    if position[0] < -25:
        score[1] += 1
        start = 1
    if position[0] > WIDTH + 25:
        score[0] += 1
        start = 1


    #----------Déplacement de la balle----------
    position[0] += position[2] * position[4]
    position[1] += position[3] * position[4]
    if position[1] < 15:
        position[3] = 1
    if position[1] > HEIGHT-15:
        position[3] = -1
    if position[1] > player2[0] and position[1] < player2[0]+60 and position[0] > WIDTH-35 and position[0] < WIDTH-20 and position[2] == 1:   #Rebond sur le pong droit
        position[2] = -1
        position[4] += 0.3
        color_ball = [0,0,225]
    if position[1] > player[0] and position[1] < player[0]+60 and position[0] < 45 and position[0] > 20 and position[2] == -1:   #Rebond sur le pong gauche
        position[2] = 1
        position[4] += 0.3
        color_ball = [225,0,0]
    pygame.draw.circle(window, color_ball, [int(position[0]), int(position[1])], 15, 3)

    #----------Déplacement des pongs----------
    #Joueur 1
    if player[0] < 10 and player[1] == -10:
        player[1] = 0
    if player[0] > HEIGHT-70 and player[1] == 10:
        player[1] = 0
    player[0] += player[1]
    pygame.draw.rect(window,(225,0,0),pygame.Rect(10,player[0],10,60),2)
    #Joueur 2
    if player2[0] < 10 and player2[1] == -10:
        player2[1] = 0
    if player2[0] > HEIGHT-70 and player2[1] == 10:
        player2[1] = 0
    player2[0] += player2[1]
    pygame.draw.rect(window,(0,0,225),pygame.Rect(WIDTH-20,player2[0],10,60),2)

    #----------Afficher le score----------
    my_font = pygame.font.Font("ressources/neon_pixel-7.ttf", 60)
    text_surface = my_font.render(str(score[0]), True, (225, 0, 0))  # Texte en bleu
    window.blit(text_surface, (WIDTH//2-30, 20))  # Positionnez le texte

    my_font = pygame.font.Font("ressources/neon_pixel-7.ttf", 60)
    text_surface = my_font.render(str(score[1]), True, (0, 0, 225))  # Texte en rouge
    window.blit(text_surface, (WIDTH//2+10, 20))  # Positionnez le texte

    if score[0] == 5:
        my_font = pygame.font.Font("ressources/neon_pixel-7.ttf", 100)
        text_surface = my_font.render("VICTOIRE DU J1", True, (225, 0, 0))  # Texte en rouge
        window.blit(text_surface, (WIDTH//2-300, 100))  # Positionnez le texte
        pygame.display.update()
        rafraichissement.tick(60)  # framerate du jeu
        time.sleep(3)
        start = 2
    if score[1] == 5:
        my_font = pygame.font.Font("ressources/neon_pixel-7.ttf", 100)
        text_surface = my_font.render("VICTOIRE DU J2", True, (0, 0, 225))  # Texte en bleu
        window.blit(text_surface, (WIDTH//2-300, 100))  # Positionnez le texte
        pygame.display.update()
        rafraichissement.tick(60)  # framerate du jeu
        time.sleep(3)
        start = 2

        

    #----------Boutons-----------
    for event in pygame.event.get():

        if event.type == QUIT:  #croix rouge
            quitter()

        if event.type == pygame.KEYDOWN:
            if event.key == K_a:
                player[1] = -10
            elif event.key == K_q:
                player[1] = 10
            if event.key == K_UP:
                player2[1] = -10
            elif event.key == K_DOWN:
                player2[1] = 10
            

        if event.type == pygame.KEYUP:
            if event.key == K_a:
                player[1] = 0
            if event.key == K_q:
                player[1] = 0
            if event.key == K_UP:
                player2[1] = 0
            if event.key == K_DOWN:
                player2[1] = 0


    pygame.display.update()
    rafraichissement.tick(60)  # framerate du jeu




