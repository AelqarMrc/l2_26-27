# On va utiliser des méthodes du module sys
import sys

# On récupère le nom de fichier donné en argument
# en ligne de commande depuis la liste argv
file_name = sys.argv[1]

# On récupère une tête de lecture sur le fichier file_name
file = open(file_name)

# On parcours le fichier file_name ligne à ligne ==> str
for line in file:
    # Si le str line commence par la chaîne ATOM
    if line.startswith("ATOM"):
        # Afficher le str line 
        # sans les caractères spéciaux 
        # de début et fin
        print(line.strip())