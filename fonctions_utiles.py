def introduction():
    print("Bienvenue dans l'univers de Fort Boyard !")
    print("Vous devez accomplir des épreuves dans différentes salles pour gagner des clés.")
    print("L'objectif : obtenir trois clés pour ouvrir la porte de la salle du trésor.")
    print("Bonne chance !")

def composer_equipe():
    equipe = []
    nb_joueur = int(input("Combien de joueur voulez vous dans votre equipe (ce chiffre ne doit pas depasser 3) ?")
    if nb_joueur < 1 and nb_joueur > 3 :
        nb_joueur = int(input("Combien de joueur voulez vous dans votre equipe (Attention ! ce chiffre ne doit pas depasser 3) ?")
    for i in range (nb_joueur):
        cle = input("Entrez une clé : ")
        valeur = input("Entrez une valeur pour cette clé : ")
        dictionnaire[cle] = valeur
        nom = input("Entrez le nom du joueur : ")
        profession = input("Entrez la profession du joueur : ")
        leader = input("Le joueur est-il le leader de l'équipe ? (oui/non) : ").lower() == 'oui'
        joueur = {
                'nom': nom,
                'profession': profession,
                'leader': leader,
                'cles_gagnees': 0  # Initialisé à zéro
        }
    equipe.append(joueur)
    if not any(joueur['leader'] for joueur in joueurs):
    # Si aucun leader n'a été désigné, le premier joueur devient le leader
        joueurs[0]['leader'] = True
    return equipe

def menu():
    print("Voici les differents types epreuve:\n1. Épreuve de Mathématiques\n2. Épreuve de Logique\n3. Épreuve du hasard\n4. Énigme du Père Fouras")
    choix = int(input("Quels types d'épreuve voulez vous faire ? "))


def choisir_joueur(equipe):
    print("Voici la liste des joueurs de l'équipe :")
    for i, joueur in enumerate(equipe, 1):
        if joueur['leader']:
            role = "Leader"
        else :
            role = "Membre"
        print(f"{i}. {joueur['nom']} ({joueur['profession']}) - {role}")
    choix = int(input("Entrez le numéro du joueur : "))
    while 1 > choix and choix > len(equipe):
        choix = int(input("Entrez le numéro du joueur : "))
    joueur_choisi = equipe[choix - 1]
    print(f"Vous avez choisi {joueur_choisi['nom']} pour participer à l'épreuve.")
    return joueur_choisi  # Retourner le joueur choisi



# Exemple d'utilisation
equipe = [
    {'nom': 'Jean Dupont', 'profession': 'Ingénieur', 'leader': True, 'cles_gagnees': 0},
    {'nom': 'Marie Martin', 'profession': 'Enseignante', 'leader': False, 'cles_gagnees': 0},
    {'nom': 'Paul Durand', 'profession': 'Docteur', 'leader': False, 'cles_gagnees': 0}
]

choisir_joueur(equipe)

