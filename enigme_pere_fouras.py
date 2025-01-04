import random
import json
def charger_enigme(fichier):
    with open(fichier, "r",encoding="utf-8") as f:
        contenu = json.load(f)
    return contenu

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
