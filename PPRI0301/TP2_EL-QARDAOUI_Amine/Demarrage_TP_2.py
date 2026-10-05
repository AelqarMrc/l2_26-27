# On importe le parser qui va analyser sys.argv
from argparse import ArgumentParser

# On importe ce qu'il faut pour tester l'existence d'un fichier
from os.path  import isfile 
import os.path
from datetime import datetime

# Pour le FASTA, c'est SeqIO (de Biopython) notre meilleur ami
from Bio import SeqIO

# Gestion automatisée des arguments
# C'est une fonction sans paramètre
def manageArguments():
    # Initialisation du parser d'arguments
    parser = ArgumentParser()

    # Création d'un paramètre obligatoire (pas de -) qui sera un str (c'est le type par défaut)
    parser.add_argument("filename",        help="Path to a FASTA file")

    # Création d'une option booléenne (option courte avec un - et/ou option longue avec --)
    # d'après le paramètre action, si l'option est fournie, sa valeur est True sinon False
    parser.add_argument("-v", "--verbose", help="Activating verbose mode", action="store_true")

    #Ajout d'option 
    parser.add_argument("--specie", type=str, help="Filtre espece")
    parser.add_argument("--minN", type=int, help="nb min d'acide aminé N")
    parser.add_argument("--maxN", type=int, help="nb max d'acide aminé N")

    # On retourne le resultat du parsing
    # C'est l'appel à parse_args qui déclenche l'analyse de sys.argv
    # La structure obtenue est un namespace (espace de nom)
    return parser.parse_args()

def validateArguments(options):
    if options.minN is not None and options.minN <= 0:
            print("Le minimum doit être strictement positif")
            exit(11)
    if options.maxN is not None and options.maxN <= 0:
            print("Le maximum doit être strictement positif")
            exit(12)
    if options.minN is not None and options.maxN is not None and options.minN > options.maxN:
            print("Le min doit être inférieur ou égale au max")
            exit(13)

def filterEntry(entry, options):
    if options.specie is not None and  options.specie not in entry.description:
        return False
    if options.minN is not None and len(entry.seq) < options.minN:
        return False
    if options.maxN is not None and len(entry.seq) > options.maxN:
        return False

    return True

def writeLog(options, results=None, error_msg=None, exit_code=0):
    if error_msg is not None:
        print(error_msg)
        print(exit_code)
        exit(30)

    if not os.path.exists("logs"):
        os.mkdir("logs")

    filename = datetime.now().strftime("%y%m%d-%H%M%S") + ".log"

    with open(os.path.join("logs", filename), "w") as f: 
        f.write(f"Paramètres : {options}\n")
        f.write(f"Nombre de séquences retenues : {len(results)}\n")

# Code principal
if __name__ == "__main__":

    # arguments contient le résultat du parsing
    options = manageArguments()

    # le nom à utiliser est celui du/des paramètre(s) obligatoire ou le nom long de l'/des options
    filename      = options.filename
    verbose_mode  = options.verbose
    specie = options.specie

    if not specie==None:
        print()

    print()
    print("Configuration:")
    # \t rajoute une tabulation à l'affichage
    print("\tFASTA file name =",filename)
    # On aurait pu écrire print(f"\tFASTA file name = {filename}")

    # verbose un paramètre qui existe toujours (True ou False)
    # par contre, un paramètre sans valeur par défaut n'existerait pas
    # dans l'espace de nom et vaudrait None s'il n'était pas fourni par l'utilisateur
    print("\tVerbose mode    =",verbose_mode)
    
    print()

    # Si le résultat de isfile est faux ... ==> on arrête là
    if not isfile(filename):
        print(f"{filename} is not a valid file name")
        exit(10)
    validateArguments(options)

    results = []

    # On lance la lecture en mode FASTA
    # avec numérotation <=> merci enumerate
    for index, entry  in enumerate(SeqIO.parse(filename,"fasta")):
        if filterEntry(entry, options) == True:
            # on affiche l'identifiant de chaque entrée précédé de sa position dans la base de données
            # attention l'affichage est décalé de 1
            print(f"Entrée {len(results)+1} : {entry.id}")

            # si le mode verbose est activé
            # le test est équivalent à : verbose_mode == True
            if verbose_mode:

                # Affichage de la description complète
                print(f"\tDescription : {entry.description}")

                # Affichage de la séquence
                print(f"\tSequence    : {entry.seq}")

            results.append(entry)
            # Une ligne vide pour séparer les entrées
            print()

        print(f"{len(results)} entrées sélectionnées")



    # Tout s'est bien passé
    exit(0)