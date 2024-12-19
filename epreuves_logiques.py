import random
def retrait_ordi(baton):
    mouv = random.choice([1, 2, 3])
    baton = baton - mouv
    print(f"l'ordinateur a pris {mouv} baton")
    print(baton * "|", baton)
    return baton

def retrait_joueur(baton):
    L = [1, 2, 3]
    n=0
    while n not in L:
        n = int(input("choisir combien de baton prendre entre 1,2 et 3 :"))
    baton = baton - n
    print(baton * "|", baton)
    return baton

def echange_joueur(joueur):
    if joueur == "joueur_1":
        joueur = "ordi"
    else:
        joueur = "joueur_1"
    return joueur

def jeu_nim_contre_ordi():
    baton = 20
    print("Bienvenue au jeu de Nim !")
    print(f"Il y a {baton} bâtons au départ. Chaque joueur peut prendre entre 1 et 3 bâtons par tour.")
    print("Le joueur qui prend le dernier bâton perd la partie.\n")
    joueur = "joueur_1"
    while baton > 0 :
        if joueur == "joueur_1" :
            baton = retrait_joueur(baton)
        else :
            baton = retrait_ordi(baton)
        joueur = echange_joueur(joueur)
    return  joueur, "a gagné"
print(jeu_nim_contre_ordi())