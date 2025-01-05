#FORT BOYARD SIMULATOR : fortpy-DEHEZ-FOURNIER-D
#DEHEZ Delphine / FOURNIER Aurélia
# Ce fichier centralise toutes les actions du jeu en utilisant les fonctions des autres modules que nous avons créés dans ce projet

from fonctions_utiles import *
from epreuves_mathematiques import epreuve_math
from epreuves_logiques import jeu_bataille_navale
from epreuves_hasard import epreuve_hasard
from enigme_pere_fouras import enigme_pere_fouras
from epreuve_finale import salle_de_tresor

#fonction déroulant le jeu
# Ouvre le fichier historique
# compose l'équipe
# boucle jusqu'à l'obtention de 3 clés lors des épreuves
# Quand les 3 clés sont trouvés, lancer l'énigme finale
def jeu():
    f=open("output/historique.txt","w")
    introduction()
    equipe = composer_equipe()
    nb_cle=0
    while nb_cle < 3 :
        epreuve = menu_epreuves()
        joueur = choisir_joueur(equipe)
        if epreuve == 1:
            res = epreuve_math()
        elif epreuve == 2:
            res = jeu_bataille_navale()
        elif epreuve == 3:
            res = epreuve_hasard()
        elif epreuve == 4:
            res =enigme_pere_fouras()
        if res == True:
            nb_cle += 1
        enregistrer_historique(f,joueur["nom"],epreuve,res,nb_cle)
    res = salle_de_tresor()
    enregistrer_historique(f,equipe[0]["nom"],"salle de tresor",res,nb_cle)
    f.close()
    return res

jeu()