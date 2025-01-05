#FORT BOYARD SIMULATOR : fortpy-DEHEZ-FOURNIER-D
#DEHEZ Delphine / FOURNIER Aurélia
# Ce fichier comporte l'épreuve du père Fouras, le joueur doit résoudre une énigme posée par le Père Fouras à l'aide de la fonction

import random
import json
#Charge le fichier des énigmes pour retourner une liste au format Json
#parametre : fichier : Chaine de caractères représentant le path du fichier
def charger_enigme(fichier):
    with open(fichier, "r",encoding="utf-8") as f:
        contenu = json.load(f)
    return contenu

#Retourne un booléen indiquant si le joueur a bien répondu à l'énigme
#si le joueur a réussi l'épreuve il gagne une clef, sinon s'il perd l'épreuve il ne gagne pas de clef
#l'énigme est choisi au hasard dans une liste
#le joueur dispose de 3 essais
def enigme_pere_fouras():
    print("Bienvenue dans l'epreuve des enigmes du Père Fouras")
    enigmes = charger_enigme("DATA/enigmesPF.json")
    enigme = random.choice(enigmes)
    essai =3
    print(enigme["question"])
    rep =""
    while essai > 0 and rep.lower() != enigme["reponse"].lower():
        rep = input(f"Vous avez {essai} essai(s).\nVotre réponse est : ")
        essai -= 1
    if rep.lower() == enigme["reponse"].lower():
        print("🎉 Bravo vous avez reussis! Vous gagnez une 🔑! 🎉")
        return True
    else:
        print("Vous n'avez pas reussi l'epreuve, Vous ne gagnez pas de 🔑. 😔")
    return False
