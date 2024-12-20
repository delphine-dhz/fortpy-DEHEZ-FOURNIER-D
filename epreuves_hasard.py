#EPREUVE HASARD : BONNETEAU

import random

def bonneteau() :
    print("Bienvenue sur l'épreuve de hasard")
    btx = ['A','B','C']
    print("Epreuve des bonneteaux : deviner sous lequel des 3 bonneteaux se trouve la clef, vous disposez de 2 essais")
    print ("Voici les bonneteaux : A , B , C")
    valide = False
    i = 2
    reponse = random.choice(btx)
    while valide == False and i >=1 :

        print("Vous avez",i,"tentatives")
        choix_joueur = input("Votre choix ? :")
        choix_joueur_maj = choix_joueur.upper()

        if choix_joueur_maj in btx :
            if choix_joueur_maj == reponse :
                print("Bonne réponse ! Vous gagnez la clé ")
                valide = True
            else :
                if i==1:
                    print("Vous avez perdu l'épreuve, la clé se trouvait sous le bonneteau",reponse)
                else:
                    print("Mauvaise réponse !Il vous reste",i-1,"tentative" )
        else :
            print("Votre choix ne fait pas parti des propositions")
        i = i - 1
    return valide

#bonneteau()

#EPREUVE HASARD 2 : LANCER DE DES

def jeu_lance_des() :
    print("Bienvenue sur l'épreuve de hasard")
    valide = False
    trouver6 = False
    i = 3
    while trouver6 == False and i>=1 :
        print("Vous avez",i," essai(s)")
        input("Lancer les dès en appuyant sur entrée")
        des_joueur = (random.randint(1, 6), random.randint(1, 6))
        print ("le joueur a obtenu :",des_joueur)
        des_maitre = (random.randint(1, 6), random.randint(1, 6))
        print ("le maitre a obtenu :",des_maitre)
        if 6 in des_joueur :
            print("Bravo vous remportez la partie ,vous avez gagné une clé !")
            trouver6 = True
            valide = True
        elif 6 in des_maitre :
            print("Perdu, le maitre du jeu remporte la partie")
            trouver6 = True
        elif i>1 :
           print ("Passons au prochain essai")
        i = i - 1
    return valide
    if valide == False :
        print("Aucun joueur n'a obtenu 6\n Match nul")
jeu_lance_des()







