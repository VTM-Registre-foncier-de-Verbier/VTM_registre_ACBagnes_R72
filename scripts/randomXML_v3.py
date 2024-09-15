# Pour faire fonctionner le code python randomXML, il faut:
# 1. Ouvrir Anaconda Prompt
# 2. Taper cd espace; cette commande permet de se déplacer pour être là où se trouve le script
# 3. Copier/coller, juste après l'espace, le chemin où se trouve le fichier qui permet la randomisation des fichiers xml.
#    Dans Windows, il suffit d'aller dans le dossier où se trouve le fichier python et de copier le nom du chemin dans la barre d'adresse.
#    Dans mon cas pour la validation du cours: C:\Users\Christine\Documents\GitHub\Depot_entrainement_VTM_Test\Depot_entrainement_VTM_Test
#    Dans mon cas pour le mini-mémoire : C:\Users\Christine\Documents\GitHub\Registre_foncier_de_Verbier\VTM_Depot_entrainement\VTM_Depot_entrainement
#    RAPPEL : le copier/coller ne fonctionne pas dans Anacond Prompt, il faut faire un clic droit pour coller le chemin.
# 4. On doit se retrouver avec ce type de commande : cd C:\Users\Christine\Documents\GitHub\Registre_foncier_de_Verbier\VTM_Depot_entrainement\VTM_Depot_entrainement
# 5. Taper Enter
# 6. Taper python suivi du nom du fichier. Dans mon cas python randomXML_v3.py
# 7. Taper Enter
# 8. Trois fichiers texte apparaissent par défaut dans le dossier où se trouve le fichier du code. Et c'est FINI!!

import os
import random
import re

# ATTENTION, ici il faut indiquer le chemin du dossier dans lequel sont déposés les fichiers .xml
pathBase=r"C:\Users\Christine\Documents\GitHub\Registre_foncier_de_Verbier\VTM_Depot_entrainement\VTM_Depot_entrainement\data"
pathVariant = os.listdir(pathBase)


train = open("train.txt", "w")
dev = open("dev.txt", "w")
test = open("test.txt", "w")

# Si on garde les mêmes chiffres (et les mêmes fichiers), la répartition est la même à chaque fois. On peut les changer au besoin.
random.seed('1214')

for i in pathVariant:
    if (".xml" in i):
        monRand = random.random()
        if monRand <= 0.1:
            test.write(i+"\n")
        elif 0.1 < monRand <= 0.2:
            dev.write(i+"\n")
        else:
            train.write(i+"\n")

test.close()
dev.close()
train.close()
