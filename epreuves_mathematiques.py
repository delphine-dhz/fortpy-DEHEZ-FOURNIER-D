#FORT BOYARD SIMULATOR : fortpy-DEHEZ-FOURNIER-D
#DEHEZ Delphine / FOURNIER Aurélia
# Ce fichier comporte les épreuves de mathématiques : premier le plus proche, équation linéaire et roulette mathématique
# La fonction finale epreuve_math chosi une épreuve aléatoirement parmi ces 3 épreuves

import random
from fonctions_utiles   import estEntier,estDecimal
# EPREUVE MATH 1 : NOMBRE PREMIER LE PLUS PROCHE
#fonction retournant un booléen si la valeur en paramètre est un nombre premier
#paramètre : n : entier
def est_premier (n) :
    premier = True
    i = 2
    while i < n and n % i != 0 :
        i = i + 1
    if i < n :
        premier = False
    return premier

#fonction retournant un entier représentant le nombre premier >= à la valeur en paramètre
#paramètre : n : entier
def premier_plus_proche(n) :
    i = n
    if est_premier(n) == False :
        while est_premier(i) == False and i <= 23 :
            i = i + 1
    return i

#retourne un booléen indiquant si le joueur a trouvé le nombre premier le plus proche d'un nombre pris au hasard entre 10 et 20
#si le joueur a réussi l'épreuve il gagne une clef, sinon s'il perd l'épreuve il ne gagne pas de clef
def epreuve_math_premier() :
    print("C'est parti, bonne chance")
    valide = bool
    n = random.randint(10, 20)
    print (" Trouver le nombre premier le plus proche et supérieur ou égal à",n)
    test = False
    while test==False :
        str = input("saisir votre réponse :")
        if estEntier(str):
            test=True
            rep=int(str)
    print("Votre réponse :",rep)
    bonnerep = premier_plus_proche(n)
    if rep == bonnerep :
        print("🎉 Bravo ! Vous gagnez une 🔑. 🎉 ")
        return True
    else :
        print ("Incorrect! Vous ne gagnez pas une 🔑. 😔 ")
    return False

#EPREUVE MATH 2 : RESOUDRE EQUATION LINEAIRE
#retourne les composants a,b,x d'une équation du type ax+b=0
#choix de a et b au hasard entre 1 et 10
def resoudre_equation_lineaire() :
    a = random.randint(1,10)
    b = random.randint(1,10)
    x = -b/a
    return a,b,x

#retourne un booléen indiquant si le joueur a pu résoudre une equation du type ax+b=0
#si le joueur a réussi l'épreuve il gagne une clef, sinon s'il perd l'épreuve il ne gagne pas de clef
def epreuve_math_equation() :
    print("C'est parti, bonne chance")
    a,b,x = resoudre_equation_lineaire()
    print("Épreuve de Mathématiques: Résoudre l'équation",a,"x +",b," = 0.")
    test=False
    while test==False :
        str =input("Saisir le resultat de cette equation :")
        if estDecimal(str):
            test=True
            rep = float(str)
    if rep == x :
        print ("🎉 Bravo ! Vous gagnez une 🔑. 🎉")
        return True
    else :
        print ("Incorrect! Vous ne gagnez pas une 🔑.😔")
    return False

#EPREUVE MATH 3 : ROULETTE MATHEMATIQUE
#retourne un booléen indiquant si le joueur a pu résoudre la suite d'opérations sur une liste de valeur
#création d'une liste de 5 entiers au hasard entre 1 et 20
#choix d'une opération entre 'addition', 'soustraction','multiplication'
#si le joueur a réussi l'épreuve il gagne une clef, sinon s'il perd l'épreuve il ne gagne pas de clef
def epreuve_roulette_mathematique() :
    print("C'est parti, bonne chance")
    roulette = [random.randint(1, 20) for _ in range(5)]
    operations = ['addition', 'soustraction','multiplication' ]
    op = random.choice(operations)
    res = roulette[0]
    if op == 'addition' :
        for i in range (1,5):
            res += roulette[i]
    elif op == 'soustraction' :
        for i in range (1,5):
            res -= roulette[i]
    elif op == 'multiplication' :
        for i in range (1,5):
            res *= roulette[i]
    print ("Nombres sur la roulette :",roulette)
    test = False
    while test==False :
        str = input(f"Calculez le résultat en combinant ces nombres avec une {op} :")
        if estDecimal(str):
            test = True
            rep = float(str)
    print ("Votre réponse :",rep)
    if res == rep :
        print ("🎉 Bravo ! Vous gagnez une 🔑 🎉")
        return True
    else :
        print ("Incorrect! Vous ne gagnez pas une 🔑. 😔")
    return False

#SELECTION DE L'EPREUVE
#retourne un booléen qui est le résultat d'une des fonctions mathématiques
#choix au hasard de la fonction parmi [epreuve_math_premier, epreuve_roulette_mathematique, epreuve_math_equation]
def epreuve_math() :
    print("Bienvenue sur l'épreuve de mathematiques")
    epreuves = [epreuve_math_premier,epreuve_roulette_mathematique,epreuve_math_equation]
    epreuve = random.choice(epreuves)
    if epreuve == epreuve_math_premier :
        return epreuve_math_premier ()
    if epreuve == epreuve_roulette_mathematique :
        return epreuve_roulette_mathematique()
    if epreuve == epreuve_math_equation :
        return epreuve_math_equation()

