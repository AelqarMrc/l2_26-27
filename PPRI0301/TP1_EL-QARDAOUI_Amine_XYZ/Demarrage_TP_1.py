# On va utiliser des méthodes du module sys
import sys
from os.path import isfile

def lire_pdb(file_name) : 
    # On récupère une tête de lecture sur le fichier file_name
        file = open(file_name)
    
        # On parcours le fichier file_name ligne à ligne ==> str
        nbAtomes = []
        for line in file:
            # Si le str line commence par la chaîne ATOM
            if line.startswith("ATOM") or line.startswith("HETATM"):

                # Afficher le str line 
                # sans les caractères spéciaux 
                # de début et fin
                symb = line[76:78].strip()
                x = line[30:38]
                y = line[38:46]
                z = line[46:54]

                x = float(x)
                y = float(y)
                z = float(z)
                myTuple=(symb,x,y,z)
                print(myTuple)

                nbAtomes.append(myTuple) 


if __name__ == "__main__" :

# On récupère le nom de fichier donné en argument
# en ligne de commande depuis la liste argv
    arguments = sys.argv[1:]

    # Vérification du nombre d'arguments
    if len(arguments) < 1 : 
        print("Il manque l'argument du fichier\n")
        exit(2)
    elif len(arguments) > 1 : 
        print("Il y'a trop d'argument !\n")
        exit(3)

    file_name = arguments[0]
    print("Il y'a le bon nombre d'argument !\n")

    if not isfile(file_name) : 
        print("Mais le fichier en argument n'existe pas...")
        exit(4)

    lire_pdb(file_name)