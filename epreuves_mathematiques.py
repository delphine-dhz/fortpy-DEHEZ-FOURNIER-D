# EPREUVE MATH 1 : NOMBRE PREMIER LE PLUS PROCHE
print("Bienvenue sur l'épreuve de mathematiques")
def est_premier (n) :
    premier = True
    i = 2
    while i < n and n % i != 0 :
        i = i + 1
    if i < n :
        premier = False
    return premier

def premier_plus_proche(n) :
    i = n
    if est_premier(n) == False :
        while est_premier(i) == False and i <= 23 :
            est_premier(i)
            i = i + 1
    return i

import random
def epreuve_math_premier() :
    n = random.randint(10, 20)
    print (" Trouver le nombre premier le plus proche de",n )
    rep = int(input("saisir votre réponse :"))
    print("Votre réponse :",rep)
    bonnerep = premier_plus_proche(n)
    if rep == bonnerep :
        print("Correct! Vous gagnez une clé. ")
    else :
        print ("Incorrect! Vous ne gagnez pas une clé. ")

#EPREUVE MATH 2 : RESOUDRE EQUATION LINEAIRE
def resoudre_equation_lineaire() :
    a = random.randint(1,10)
    b = random.randint(1,10)
    x = -b/a
    return a,b,x

def epreuve_math_equation() :
    a,b,x = resoudre_equation_lineaire()
    print("Épreuve de Mathématiques: Résoudre l'équation",a,"x +",b," = 0.")
    rep = float(input("Saisir le resultat de cette equation :"))
    print("Quelle est la valeur de x:",rep )
    if rep == x :
        return True
    else :
        return False

#EPREUVE MATH 3 : ROULETTE MATHEMATIQUE
def epreuve_roulette_mathematique() :
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
    rep = int(input(f"Calculez le résultat en combinant ces nombres avec une {op} :"))
    print ("Votre réponse :",rep)
    if res == rep :
        return True
    else :
        return False

#SELECTION DE L'EPREUVE

def epreuve_math() :
    epreuves = [epreuve_math_premier,epreuve_roulette_mathematique,epreuve_math_equation]
    epreuve = random.choice(epreuves)
    return epreuve

jeu= epreuve_math()
if jeu() == True :
    print("Bonne réponse! Vous gagnez une clé. ")
else :
    print("Mauvaise réponse! Vous ne gagnez pas une clé. ")



#if __name__ == '__main__' :
#TEST MATH 1
    #epreuve_math_premier()
#TEST MATH 2
    #if epreuve_math_equation() == True:
        #print("Bonne réponse! Vous gagnez une clé. ")
    #else:
        #print("Mauvaise réponse! Vous ne gagnez pas une clé. ")
#TEST MATH 3
    #if  epreuve_roulette_mathematique() == True:
        #print("Bonne réponse! Vous gagnez une clé. ")
    #else:
        #print("Mauvaise réponse! Vous ne gagnez pas une clé. ")