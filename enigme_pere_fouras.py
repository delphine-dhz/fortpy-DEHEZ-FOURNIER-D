import random
import json

def question_pf(fichier):
    with open(fichier, "r",encoding="utf-8") as f:
        contenu = json.load(f)
    choix = random.choice(contenu)
    print("Bienvenue dans l'epreuve des enigmes du Père Fouras")
    question, reponse = choix["question"], choix["reponse"]
    print(question)
    essai = 3
    rep = input(f"Vous avez {essai} essai(s).Votre réponse est : ")
    while rep.lower() != reponse.lower() and essai != 0 :
        essai -= 1
        rep = input(f"Vous avez plus que {essai} essai(s).Votre réponse est : ")
    if rep.lower() == reponse.lower():
        return "Bravo vous avez reussis! Vous avez gagné une clé."
    else :
        return "Vous n'avez pas reussi l'epreuve."

path = "data/enigmesPF.json"

print(question_pf(path))