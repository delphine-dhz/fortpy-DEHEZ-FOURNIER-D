import random
import json

def salle_de_tresor():
    fichier = "DATA/indicesSalle.json"
    with open(fichier, "r", encoding="utf-8") as f:
        jeu_tv = json.load(f)
    annee = random.choice(list(jeu_tv["Fort Boyard"].keys()))
    print("Année sélectionnée : ",annee)
    emission = random.choice(list(jeu_tv["Fort Boyard"][annee].keys()))
    print("Emisson sélectionnée : ",emission)
    indices = jeu_tv["Fort Boyard"][annee][emission]["Indices"]
    print("Bienvenue dans la salle du trésor de Fort Boyard !")
    print("Voici les trois premiers indices pour deviner le mot-code :")
    indices_donnes = random.sample(indices, 3)
    print(indices_donnes)
    mot_code = jeu_tv["Fort Boyard"][annee][emission]["MOT-CODE"]
    essais = 3
    reponse_correcte = False
    while essais > 0 and reponse_correcte == False :
        mot_devine = input(f"Vous avez {essais} essai(s). Quelle est votre réponse ? ")
        if mot_code.lower() == mot_devine.lower() :
            reponse_correcte = True
        else :
            essais -= 1
            if essais>0:
                indice =""
                i=0
                while indice=="":
                    if(indices[i] not in indices_donnes):
                        indice=indices[i]
                        indices_donnes.append(indice)
                    i += 1
                print("Voici un indice supplémentaire : ",indice)
    if reponse_correcte == True :
        print("🎉 Bravo ! Vous avez reussi à ouvrir la salle du trésor. 🎉")
        return True
    else :
        print("Malheuresement, vous n'avez pas reussi à ouvrir la salle du trésor.😔")
        print("La réponse était : ",mot_code)
    return False
