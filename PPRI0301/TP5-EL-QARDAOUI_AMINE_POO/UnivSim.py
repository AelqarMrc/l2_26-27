import math


class Salle:
    _dernier_numero = 0

    def __init__(self, nom: str, capacite: int):
        self.nom = nom
        self.__occupants = 0
        if capacite > 0:
            self.__capacite = capacite
        else:
            self.__capacite = 1  # Valeur par défaut
            print("Avertissement : La capacité doit être supérieure à 0.")
        Salle._dernier_numero += 1
        self.__numero = Salle._dernier_numero


    def entrer(self, n: int) -> None:
        if self.__occupants + n > self.__capacite:
            print(f"Avertissement : Capacité maximale dépassée pour {self.nom} ({self.__occupants + n}/{self.__capacite}). Entrée refusée.")
        else:
            self.__occupants += n

    def sortir(self, n: int) -> None:
        self.__occupants = max(0, self.__occupants - n)

    def est_pleine(self) -> bool:
        return self.__occupants >= self.__capacite

    def get_occupants(self) -> int:
        return self.__occupants

    def get_numero(self) -> int:
        return self.__numero

    def get_capacite(self) -> int:
        return self.__capacite

    def set_capacite(self, valeur: int) -> None:
        if valeur <= 0:
            print("Erreur : La capacité doit être strictement supérieure à 0.")
        else:
            self.__capacite = valeur

    @classmethod
    def from_texte(cls, texte: str) -> "Salle":
        nom, capacite_str = texte.split(";")
        return cls(nom, int(capacite_str))

    @staticmethod
    def est_rentable(capacite: int) -> bool:
        return capacite >= 20

class Amphi(Salle):
    def __init__(self, nom: str, capacite: int, micro: bool):
        super().__init__(nom, capacite)
        self.micro = micro

    def entrer(self, n: int) -> None:
        limite_securite = math.floor(self.get_capacite() * 0.90)
        
        if self.get_occupants() + n > limite_securite:
            print(f"Avertissement (Incendie) : Entrée refusée dans {self.nom}. "
                  f"Capacité de sécurité dépassée ({self.get_occupants() + n}/{limite_securite}).")
        else:
            super().entrer(n)


class SalleTP(Salle):
    def __init__(self, nom: str, capacite: int, nb_postes: int):
        super().__init__(nom, capacite)
        self.nb_postes = nb_postes

    def entrer(self, n: int) -> None:
        postes_libres = max(0, self.nb_postes - self.get_occupants())
        entrants_effectifs = min(n, postes_libres)

        if entrants_effectifs < n:
            print(f"Information : Seules {entrants_effectifs} personne(s) sur {n} peuvent entrer dans {self.nom} (limite de postes).")

        if entrants_effectifs > 0:
            super().entrer(entrants_effectifs)


class CourtDeSport:
    def __init__(self, nom: str, surface: float):
        self.nom = nom
        self.surface = surface
        self.occupants = 0

    def entrer(self, n: int) -> None:
        # Pas de limite de capacité
        self.occupants += n
        print(f"{n} personnes sont entrées sur le court {self.nom} ({self.occupants} actuellement).")

if __name__ == "__main__":
    # PARTIE 3
    # s = Salle("D101", 30)
    # s.entrer(25) 
    # s.entrer(10) 
    # print(s.get_occupants()) 
    # s.sortir(40)  
    # print(s.get_occupants()) 


    # PARTIE 2
    # salle_info = Salle("Salle_2_R-18", 28)
    # amphi_info = Salle.from_texte("E_2_R-05;180")

    # print(f"Salle 1 -> Nom : {salle_info.nom}, N° : {salle_info.get_numero()}, Capacité : {salle_info.get_capacite()}")
    # print(f"Salle 2 -> Nom : {amphi_info.nom}, N° : {amphi_info.get_numero()}, Capacité : {amphi_info.get_capacite()}\n")

    # salle_info.entrer(20)
    # print(f"Occupants Salle_2_R-18 : {salle_info.get_occupants()}")

    # salle_info.entrer(12) 
    # print(f"Occupants Salle_2_R-18 après tentative : {salle_info.get_occupants()}")

    # salle_info.sortir(8)
    # print(f"Occupants Salle_2_R-18 après sortie : {salle_info.get_occupants()}\n")

    # amphi_info.entrer(150)
    # print(f"Occupants E_2_R-05 : {amphi_info.get_occupants()}")

    # amphi_info.sortir(200)
    # print(f"Occupants E_2_R-05 après sortie massive : {amphi_info.get_occupants()}")

    # PARTIE 3
    campus = [
        Salle("Salle_2_R-18", 35),
        Salle("Salle_1_R-02", 25),
        Amphi("E_2_R-05", 100, micro=True),
        SalleTP("Labo_Info_01", 30, nb_postes=24),
        CourtDeSport("Terrain_Synthetique", 800.0)
    ]

    # Simulation de la rentrée : 30 personnes essaient d'entrer dans chaque lieu
    print("--- Début de la simulation de rentrée (30 personnes par salle) ---\n")
    for lieu in campus:
        print(f"Tentative d'entrée dans : {lieu.nom}")
        lieu.entrer(30)
        print("-" * 50)