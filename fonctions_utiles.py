#FORT BOYARD SIMULATOR : fortpy-DEHEZ-FOURNIER-D
#DEHEZ Delphine / FOURNIER Aurélia
# Ce fichier contient plusieurs fonctions qui géreront les joueurs, les épreuves, et l'enregistrement des résultats du jeu. Ces fonctions seront utilisées pour organiser et suivre le déroulement du jeu

#affiche les consignes du jeu
def introduction():
    print("Bienvenue dans l'univers de Fort Boyard !")
    print("Vous devez accomplir des épreuves dans différentes salles pour gagner des clés.")
    print("L'objectif : obtenir trois clés pour ouvrir la porte de la salle du trésor.")
    print("Bonne chance !")

#retourne une liste de joueur ==> équipe
#composition de l'équipe par saisi du nom, profession et indicateur leader
#l'équipe est composé entre 1 et 3 membres
def composer_equipe():
    equipe = []
    test = False
    nb_leader=0
    nb_joueur=0
    while test == False :
        str = input("Combien de joueur voulez vous dans votre equipe (ce chiffre ne doit pas depasser 3) ?")
        if estEntier(str) :
            nb_joueur = int(str)
        if nb_joueur >= 1 and nb_joueur <= 3 :
            test = True
    for i in range (nb_joueur) :
        nom = input("Entrez le nom du joueur : ")
        profession = input("Entrez la profession du joueur : ")
        leader = False
        #si aucun leader on pose la question
        if nb_leader == 0:
            leader = input("Le joueur est-il le leader de l'équipe ? (oui/non) : ").lower() == 'oui'
        if leader == True:
            nb_leader += 1
        joueur = {
                'nom': nom,
                'profession': profession,
                'leader': leader,
                'cles_gagnees': 0  # Initialisé à zéro
                }
        equipe.append(joueur)
    # Si aucun leader n'a été désigné, le premier joueur devient le leader
    if nb_leader==0:
        equipe[0]['leader'] = True
    return equipe

#retourne un entier représentant le choix d'une épreuve
#Affichage des épreuves
#sélection par le joueur de l'épreuve
def menu_epreuves():
    print("Voici les differents types epreuve:\n1. Épreuve de Mathématiques🔢\n2. Épreuve de Logique🧠\n3. Épreuve du hasard🍀\n4. Énigme du Père Fouras🧙‍♂️")
    choix=0
    sel=""
    while choix ==0 :
        sel = input("Quels types d'épreuve voulez vous faire ? ")
        if estEntier(sel) :
            choix = int(sel)
    return choix

#Retourne un entier représentant l'indice dans la liste (equipe) du joueur retenu
#paramètre : equipe , liste des joueurs
def choisir_joueur(equipe):
    print("Voici la liste des joueurs de l'équipe :")
    i=1
    for joueur in equipe:
        if joueur['leader']:
            role = "Leader"
        else :
            role = "Membre"
        print(i,".", joueur['nom'], "(",joueur['profession'],") - ",role)
        i += 1
    choix = 0
    sel =""
    while choix < 1 or choix > len(equipe):
        sel = input("Entrez le numéro du joueur : ")
        if estEntier(sel):
            choix = int(sel)
    joueur_choisi = equipe[choix - 1]
    print("Vous avez choisi ",joueur_choisi['nom']," pour participer à l'épreuve.")
    return joueur_choisi  # Retourner le joueur choisi

#enregistre dans un fichier les informations du jeu
#paramètre :
# f : descripteur du fichier
# joueur : nom du joueur
# épreuve : entier représentant l'épreuve
# res : booléen indiquant si l'épreuve est réussi
# cle : le nombre de clé
def enregistrer_historique(f,joueur,epreuve,res,cle):
    f.write(joueur+";"+str(epreuve)+";"+str(res)+";"+str(cle)+"\n")

# retourne un booléen indiquant si la chaine de caractère en paramètre est un entier
# paramètre val : chaine de caractère
def estEntier(val):
    if len(val) == 0 :
        return False
    for i in range (len(val)):
        if val[i]<'0' or val[i]>'9':
            return False
    return True

# retourne un booléen indiquant si la chaine de caractère en paramètre est un decimal
# paramètre val : chaine de caractère
def estDecimal(val):
    nbdec=0
    #chaine vide retourne faux
    if len(val)==0:
        return False
    #analyse le premier caractère qui peut être numerique ou - . ,
    if (val[0] < '0' or val[0] > '9')  and val[0] not in {'.',',','-'}:
        return False
    if val[0] in {'.',','}:
        nbdec=1
    # analyse les autres caractères
    for i in range (1,len(val)):
        #un seul point autorisé
        if(val[i]=='.' or val[i]==',') :
            nbdec += 1
        elif val[i] < '0' or val[i] > '9' :
            return False
        if nbdec >1:
            return False
    return True

#print("test fonction estEntier :")
#print('123:',estEntier('123'))
#print('12a:',estEntier('12a'))
#print(':',estEntier(''))
#print("test fonction estDecimal :")
#print('123:',estDecimal('123'))
#print('123.05:',estDecimal('123.05'))
#print('-123.05:',estDecimal('-123.05'))
#print('12a.05:',estDecimal('12a.05'))
#print('123.A0:',estDecimal('123.A0'))
#print('1.3.0:',estDecimal('1.3.0'))
#print('-.12',estDecimal('-.12'))
#print(':',estDecimal(''))
