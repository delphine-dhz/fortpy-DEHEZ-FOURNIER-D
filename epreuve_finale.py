import random
import json

def salle_de_tresor():
    with open(fichier, "r", encoding="utf-8") as f:
        contenu = json.load(f)
    annee = random.choice(list(fort_boyard.keys()))
    print(f"Année sélectionnée : {annee}")
    emission = random.choice(list(fort_boyard[annee].keys()))
    print(f"Emisson sélectionnée : {emission}")
    indices = fort_boyard[annee][emission]["Indices"]
    print("Bienvenue dans la salle du trésor de Fort Boyard !")
    print("Voici les trois premiers indices pour deviner le mot-code :")
    print(random.sample(indices, 3))
    mot_code = fort_boyard[annee][emission]["MOT-CODE"]
    essai = 3
    mot_devine = input(f"Vous avez {essai} essai(s). Quelle est votre réponse ? ")
    while mot_code.lower() != mot_devine.lower() and essai != 0 :
        essai -= 1
        mot_devine = input(f"Vous avez plus que {essai} essai(s).Quelle est votre réponse ? ")
    if mot_code.lower() == mot_devine.lower():
        return "Bravo ! Vous avez reussi à ouvrir la salle du trésor."
    else :
        return "Malheuresement, vous n'avez pas reussi à ouvrir la salle du trésor."



path = "data/indicesSalle.json"
print(question_pf(path))