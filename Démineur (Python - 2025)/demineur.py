# 0 à 9 chiffre - -1 caché - -2 caché miné - -3 drapeau - -4 drapeau miné - -5 explosion

import pygame
import random
import sys

# ========== Fonctions ==========
def initialiser_tableau():
    global tableau, compteur, en_jeu
    tableau = [[-1]*30 for i in range(16)]
    compteur = 0
    # Insertion aléatoire des 99 mines
    while compteur != 99:
        pos = [random.randint(0,29),random.randint(0,15)]
        if tableau[pos[1]][pos[0]] == -1:
            tableau[pos[1]][pos[0]] = -2
            compteur += 1
    compteur = 30 * 16 - 99 # Cases non minées
    print("Tableau initialisé.")
    en_jeu = True


def pos_drapeau(x, y):
    if tableau[y][x] == -1:
        tableau[y][x] = -3
    elif tableau[y][x] == -3:
        tableau[y][x] = -1
    elif tableau[y][x] == -2:
        tableau[y][x] = -4
    elif tableau[y][x] == -4:
        tableau[y][x] = -2
         

def afficher_case(pos_x, pos_y):
    nombre_mines = -1
    # Case minée
    if tableau[pos_y][pos_x] == -2:
        tableau[pos_y][pos_x] = -5
        global en_jeu
        en_jeu = False
        return

    # Case non minée
    elif tableau[pos_y][pos_x] == -1:
        nombre_mines = 0
        for y in range(3):
            for x in range(3):
                try:
                    if (tableau[pos_y-1+y][pos_x-1+x] == -2 or tableau[pos_y-1+y][pos_x-1+x] == -4) and not ((pos_x == 0 and x == 0) or (pos_y == 0 and y == 0)):
                        nombre_mines += 1
                except IndexError:
                    pass
        tableau[pos_y][pos_x] = nombre_mines

    # Si aucune mine autour, afficher les cases adjacentes
    if nombre_mines == 0:
        for y in range(3):
            for x in range(3):
                try:
                    if tableau[pos_y-1+y][pos_x-1+x] == -1 and not ((pos_x == 0 and x == 0) or (pos_y == 0 and y == 0)):
                        afficher_case(pos_x-1+x, pos_y-1+y)
                except IndexError:
                    pass


# ========== Initialisation ==========
pygame.init()
# Définition de la taille de la fenêtre
ecran = pygame.display.set_mode((20*30, 20*16))
pygame.display.set_caption("Démineur")

# Horloge pour contrôler le taux de rafraîchissement
clock = pygame.time.Clock()
FPS = 60

# Initialisation des variables
tableau = [[-1]*30 for i in range(16)]
taille = [16,30]
compteur = 0
clic = False
en_jeu = True
couleur = [(0, 66, 255),(6, 232, 0),(255, 21, 0),(48, 0, 214),(110, 42, 0),(255, 247, 0),(0, 255, 249),(255, 0, 0)]

initialiser_tableau()

# ========== Boucle principale ==========
while True:
    # --- Affichage ---
    for y in range(taille[0]):
        for x in range(taille[1]):
            if tableau[y][x] <= 0:
                pygame.draw.rect(ecran, (150,150,150), pygame.Rect(x*20, y*20, 19, 19))
            if tableau[y][x] == -3 or tableau[y][x] == -4:
                pygame.draw.rect(ecran, (0,0,0), pygame.Rect(x*20+5, y*20+2, 2, 16))
                pygame.draw.rect(ecran, (255,0,0), pygame.Rect(x*20+7, y*20+2, 5, 5))
            if tableau[y][x] == -5:
                pygame.draw.rect(ecran, (255,0,0), pygame.Rect(x*20, y*20, 19, 19))
            if tableau[y][x] > 0:
                pygame.draw.rect(ecran, (200,200,200), pygame.Rect(x*20, y*20, 19, 19))
                font = pygame.font.Font(None, 24)
                text = font.render(str(tableau[y][x]), True, couleur[tableau[y][x]-1])
                ecran.blit(text, (x*20+5, y*20+2))
            if tableau[y][x] == 0:
                pygame.draw.rect(ecran, (200,200,200), pygame.Rect(x*20, y*20, 19, 19))

    if compteur == 0 and en_jeu:
        en_jeu = False
    if not en_jeu:
        font = pygame.font.Font(None, 48)
        if compteur == 0:
            text = font.render("Gagné !", True, (0, 255, 0))
        else:
            text = font.render("Perdu !", True, (255, 0, 0))
        ecran.blit(text, (200, 150))


    # --- Gestion des événements ---
    # Clic sur la croix
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Détection clic souris
        if event.type == pygame.MOUSEBUTTONDOWN and clic == False:
            clic = True
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if event.button == 1:  # Clic gauche
                afficher_case(mouse_x//20, mouse_y//20)
            elif event.button == 3:  # Clic droit
                pos_drapeau(mouse_x//20, mouse_y//20)

        if event.type == pygame.MOUSEBUTTONUP and en_jeu:
            clic = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                initialiser_tableau()
    
    pygame.display.flip()  # Met à jour l’affichage
    clock.tick(FPS)  # Contrôle de la boucle
