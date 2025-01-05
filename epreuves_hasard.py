#FORT BOYARD SIMULATOR : fortpy-DEHEZ-FOURNIER-D
#DEHEZ Delphine / FOURNIER Aurélia
# Ce fichier comporte les épreuves de hasard : bonneteau et lancés de dés
# La fonction finale epreuve_hasard chosie une épreuve aléatoirement parmi ces 3 épreuves
import random

#EPREUVE HASARD : BONNETEAU

#retourne un booléen indiquant si le joueur a trouvé la clef
#si le joueur a réussi l'épreuve il gagne une clef, sinon s'il perd l'épreuve il ne gagne pas de clef
#le joueur dispose de 2 essais
def bonneteau() :
    print("Bienvenue sur l'épreuve de hasard")
    btx = ['A','B','C']
    print("Epreuve des bonneteaux : deviner sous lequel des 3 bonneteaux se trouve la clef, vous disposez de 2 essais")
    print("C'est parti, bonne chance")
    print("Premier essai")
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
                print("🎉 Bonne réponse ! Vous gagnez la clé 🎉 ")
                valide = True
            else :
                if i==1:
                    print("Vous avez perdu l'épreuve, la 🔑 se trouvait sous le bonneteau",reponse,"😔")
                else:
                    print("Mauvaise réponse !Il vous reste",i-1,"tentative" )
        else :
            print("Votre choix ne fait pas parti des propositions")
        i = i - 1
    if valide == False :
        print ("Incorrect! Vous ne gagnez pas une clé.😔 ")
    return valide

#EPREUVE HASARD 2 : LANCER DE DES
#retourne un booléen indiquant si le joueur a réussi à avoir un 6 sur 3 essais
#si le joueur a réussi l'épreuve il gagne une clef, sinon s'il perd l'épreuve il ne gagne pas de clef
def jeu_lance_des() :
    print("Bienvenue sur l'épreuve de hasard")
    print ("Le premier joueur qui obtient un 6 gagne.")
    print("C'est parti, bonne chance")

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
            print("🎉 Bravo vous remportez la partie ,vous avez gagné une 🔑 ! 🎉")
            trouver6 = True
            valide = True
        elif 6 in des_maitre :
            print("Perdu, le maitre du jeu remporte la partie, vous ne gagnez pas de 🔑 😔")
            trouver6 = True
        elif i>1 :
           print ("Passons au prochain essai")
        i = i - 1
    if valide == False :
        print("Aucun joueur n'a obtenu 6\n Match nul")
    return valide

#Retourne un booléen
#appel une des 2 épreuves au hasard
def epreuve_hasard() :
    epreuves = [bonneteau, jeu_lance_des]
    epreuve = random.choice(epreuves)

    if epreuve == jeu_lance_des :
     return jeu_lance_des ()
    if epreuve == bonneteau :
        return bonneteau()







