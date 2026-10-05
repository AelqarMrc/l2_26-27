# On importe le parser qui va analyser sys.argv
from argparse import ArgumentParser, Namespace

# On importe ce qu'il faut pour tester l'existence d'un fichier
from os.path  import isfile, basename

# shutil servira pour obtenir la largeur du terminal
import shutil

def manageArguments() -> Namespace :
    """ Tool function to manage the arguments with the argparse library

    Returns:
        Namespace: the couples name/value of the parameters (from sys.argv)
    """

    # Initialisation du parser d'arguments
    parser = ArgumentParser()

    # Création d'un paramètre obligatoire (pas de -) qui sera un str (c'est le type par défaut)
    parser.add_argument("filename",        help="Path to a WFN file")

    # Création d'une option booléenne (option courte avec un - et/ou option longue avec --)
    # d'après le paramètre action, si l'option est fournie, sa valeur est True sinon False
    parser.add_argument("-v", "--verbose", help="Activating verbose mode", action="store_true")

    # On retourne le resultat du parsing
    # C'est l'appel à parse_args qui déclenche l'analyse de sys.argv
    # La structure obtenue est un namespace (espace de nom)
    return parser.parse_args()

def print_2nd_line_information(second_line : str, terminal_width : int = 160) :
    """ Tool procedure which prints data extracted from a given str

    Args:
        second_line (str): The second line of a WFN file
        terminal_width (int, default 160) : The width of the terminal in [2,160]
    """

    # On affiche 100 caractère =
    print(100*"=")

    print(f"Current terminal width: {terminal_width}")
    if terminal_width < 2 or terminal_width > 160:
        print(f"The terminal_width has a too low/high value: {terminal_width}")
        print("The width has to be in the interval [2,160]")
        print("==> Default value has been set: 160")
        terminal_width = 160

    nb_characters_by_line : int = int(terminal_width/2)
    print(f"Number of characters on each line: {nb_characters_by_line}")  

    #print(f"Second line = \n>>{second_line:80s}<<")

    print(100*"+")
    print("Fortran original format: 'GAUSSIAN',10X,I5,' MOL ORBITALS',1X,I6,' PRIMITIVES', 4X,I5,' NUCLEI'")
    print(100*"+")

    print(100*"-")

    current_index : int = 0
    while(current_index<len(second_line)):
        # avec ce test, on retourne à la ligne dès qu'on atteint
        # le nombre maximum de caractères par ligne
        if (current_index+1) % nb_characters_by_line == 0:
            print()
        # chaque lettre est affichée sur 2 caractères
        # pour s'aligner avec le 2nd affichage
        print(f"{second_line[current_index]:>2s}",end="")
        current_index+=1

    print()

    i : int = 0
    while(i<len(second_line)):
        # avec ce test, on retourne à la ligne dès qu'on atteint
        # le nombre maximum de caractères par ligne
        if (i+1) % nb_characters_by_line == 0:
            print()
        # le format "d" correspond bien à des nombres décimaux
        print(f"{i:2d}",end="")
        i+=1

    print()
    print(100*"-")

    ################################################################
    # Version du code sans tenir compte de la taille du terminal
    # Finalement un str c'est juste une liste de caractères
    # for caractere in second_line:
        # chaque lettre est affiché sur 2 caractères
        # pour s'aligner avec le 2nd affichage
    #    print(f"{caractere:>2s}",end="")
    # print()
    # on va juste numéroter (en indice) les lettres du précédent affichage
    # for i in range(80):
        # le format "d" correspond bien à des nombres décimaux
    #   print(f"{i:2d}",end="")
    # print()
    ################################################################

    print("According to the original Fortran format")
    print("the second line of the WFN file contains these information:")
    print(f"\tIndex  0 to  8 (excluded) : >>{second_line[ 0: 8]}<<")
    print(f"\tIndex  8 to 19 (excluded) : >>{second_line[ 8:19]}<<")
    print(f"\tIndex 19 to 23 (excluded) : >>{second_line[19:23]}<<")
    print(f"\tIndex 23 to 36 (excluded) : >>{second_line[23:36]}<<")
    print(f"\tIndex 36 to 37 (excluded) : >>{second_line[36:37]}<<")
    print(f"\tIndex 37 to 43 (excluded) : >>{second_line[36:43]}<<")
    print(f"\tIndex 43 to 54 (excluded) : >>{second_line[43:54]}<<")
    print(f"\tIndex 54 to 58 (excluded) : >>{second_line[54:58]}<<")
    print(f"\tIndex 58 to 63 (excluded) : >>{second_line[58:63]}<<")
    print(f"\tIndex 63 to 70 (excluded) : >>{second_line[63:70]}<<")

    # On affiche 100 caractère =
    print(100*"=")

def get_nb_orbitals_primitives_nuclei(second_line : str) \
                        -> None | tuple[int,int,int] :

    try :
        nb_orbitals   : int = int(second_line[19:23])
        nb_primitives : int = int(second_line[36:43])
        nb_nuclei     : int = int(second_line[58:63])
    except ValueError:
        return None
    else:
        return nb_orbitals,nb_primitives,nb_nuclei

def extract_nuclei(buffer, nb_nuclei: int) -> None | list[dict]:
    nuclei: list[dict] = []

    try :
        for _ in range(nb_nuclei):
            line = next(buffer)

            x_str = line[24:36].rstrip("\r\n").replace("D", "E").replace("d", "e")
            y_str = line[36:48].rstrip("\r\n").replace("D", "E").replace("d", "e")
            z_str = line[48:60].rstrip("\r\n").replace("D", "E").replace("d", "e")
            q_str = line[71:].rstrip("\r\n").replace("D", "E").replace("d", "e")

            nuclei.append({
                "symbol": line[0:4].strip(),
                "x": float(x_str),
                "y": float(y_str),
                "z": float(z_str),
                "charge": float(q_str),
            })
    except ValueError:
        return None
    else :
        return nuclei

# Code principal
if __name__ == "__main__":

    # arguments contient le résultat du parsing
    options : Namespace = manageArguments()

    # le nom à utiliser est celui du/des paramètre(s) obligatoire(s) ou le nom long de l'/des options
    filename     : str  = options.filename
    verbose_mode : bool = options.verbose

    print()
    print("Configuration:")
    print(f"\tWFN file name: {basename(filename)}")
    print("\tVerbose mode :",verbose_mode)
    print()

    # Si le résultat de isfile est faux ... ==> on arrête là
    if not isfile(filename):
        print(f"{filename} is not a valid path to a file")
        exit(10)

    # On vérifie l'extension
    if not filename.endswith(".wfn") :
        print(f"{basename(filename)} does not seem to be a WFN file.")
        exit(20)

    # Mes futures données
    nb_orbitals   : int = 0
    nb_primitives : int = 0
    nb_nuclei     : int = 0

    # un bloc pour éviter d'oublier la fermeture du lecteur de fichier
    with open(filename) as buffer:

        # grâce à la méthode "next", je contrôle l'avancement de la lecture (par ligne)
        # strip enlève les caractères spéciaux à la fin du str
        # renvoyé par next.
        current_line : str = next(buffer).strip()

        if verbose_mode :
            # Première ligne <=> description
            print(f"First line (description) = \n\t>>{current_line}<<")

        # Seconde ligne ==> celle-ci contient des info utiles
        current_line = next(buffer).strip()

        if verbose_mode:
            # On affiche des info en accord avec le format Fortran(sans vérification)
            # le caractère "\" permet de continuer une instruction sur la
            # ligne suivante
            print_2nd_line_information(current_line,\
                                       shutil.get_terminal_size().columns)

        # values peut être vide ou contenir un tuple
        values : None | tuple[int,int,int] = \
            get_nb_orbitals_primitives_nuclei(current_line)

        # Si values vaut None, c'est que l'extraction a échoué
        if values == None:
            print(f"Format error in second line of file {basename(filename)}")
            exit(30)

        # On fait un petit unpacking ;-)
        nb_orbitals, nb_primitives, nb_nuclei = values

        print("Current values :")
        print(f"\tNumber of orbitales : {nb_orbitals  :3d}")
        print(f"\tNumber of primitives: {nb_primitives:3d}")
        print(f"\tNumber of nuclei    : {nb_nuclei    :3d}")
        print()

        print(extract_nuclei(buffer, 6))

    exit(0)