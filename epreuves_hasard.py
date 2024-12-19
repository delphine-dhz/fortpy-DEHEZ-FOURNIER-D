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

bonneteau()

#E





