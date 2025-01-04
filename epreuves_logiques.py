import winsound
import random
from fonctions_utiles import isEntier
def suiv(joueur):
    if joueur == 0:
        return 1
    return 0

def grille_vide():
    size = 3
    grille=[[' ' for i in range(size)] for j in range(size)]
    return grille

def affiche_grille(grille, message) :
    print(message)
    ligne=''
    for i in range (3) :
        ligne = '|'
        for j in range (3) :
            ligne += grille[i][j]+'|'
        print(ligne)
    print('-------')

def demande_position() :
    test = False
    while not test:
        a = -1
        b = -1
        coord = input("Entrez la position (ligne,colonne) entre 1 et 3 (ex: 1,2) :")
        val = coord.split(',')
        if len(val) == 2 :
            if isEntier(val[0]) :
                a=int(val[0])-1
            if isEntier(val[1]) :
                b=int(val[1])-1
            if (a >= 0) and (a < 3) and (b >= 0) and (b < 3):
                test = True
        else :
            print("hors limite, ressaisir les coordonnées")
    return a,b

def init():
    print("positionnez vos bateaux :")
    grille = grille_vide()
    for i in range(2) :
        print("Bateau ",i+1)
        test = False
        while not test :
            a,b = demande_position()
            if grille[a][b] != ' ':
                print("position déjà prise")
            else :
                test = True
                grille[a][b] = '⛵'
    return grille

def init_aleatoire():
    grille = grille_vide()
    for i in range(2) :
        test = False
        while not test :
            a = random.randint(0,2)
            b = random.randint(0,2)
            if grille[a][b] == ' ':
                test = True
                grille[a][b] = '⛵'
    return grille

def tour(joueur, grille_tirs,grille_adversaire) :
    if (joueur == 0) :
        print("C'est à votre tour de faire feu !:")
        affiche_grille(grille_tirs, "Rappel de l'historique des tirs que vous avez effectués : ")
        a,b = demande_position()
    else :
        print("C'est le tour du maître du jeu :")
        test = False
        while test==False :
            a = random.randint(0,2)
            b = random.randint(0,2)
            if grille_tirs[a][b] == ' ':
                    test= True
        print("Le maître du jeu tire en position ",a+1,b+1)
    if grille_adversaire[a][b] == '⛵' :
        print("Touché coulé !")
        grille_tirs[a][b] = '💥'
        if(joueur == 0) :
            winsound.Beep(440,250)
        else :
            winsound.Beep(880,250)
    else :
        print("Dans l'eau...")
        grille_tirs[a][b] = '🌊'

def gagne(grille_tirs_joueur) :
    nb=0
    for i in range(3) :
        for j in range(3) :
            if(grille_tirs_joueur[i][j] == '💥') :
                nb+=1
    return nb==2

def jeu_bataille_navale():
    print("Chaque joueur doit placer 2 bateaux sur une grille de 3x3.\nLes bateaux sont représentés par '⛵' et les tirs manqués par '🌊'. \nLes bateaux coulés sont marqués par '💥'.")
    grille_joueur = init()
    affiche_grille(grille_joueur, "Découvrez votre grille de jeu avec vos bateaux :")
    grille_maitre = init_aleatoire()
    #affiche_grille(grille_maitre, "Grille du Maitre")
    tirs_joueur = grille_vide()
    tirs_maitre = grille_vide()
    fin = False
    joueur = 0
    while not fin :
        if joueur == 0:
            tour(joueur,tirs_joueur,grille_maitre)
            fin = gagne(tirs_joueur)
            if(fin == True) :
                print("🎉 Bravo vous remportez la partie ,vous gagnez une 🔑 !🎉")
        else :
            tour(joueur,tirs_maitre,grille_joueur)
            fin = gagne(tirs_maitre)
            if(fin == True) :
                print("Perdu, le maitre du jeu remporte la partie, vous ne gagnez pas de 🔑. 😔")
        if not fin :
            joueur = suiv(joueur)
    return joueur == 0

