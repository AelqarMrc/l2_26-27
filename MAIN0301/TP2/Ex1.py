import math
import matplotlib.pyplot as plt


# Données
echantillon = [
    10, 15, 10, 10, 23, 15, 42, 10, 35, 15,
    10, 35, 42, 35, 10, 15, 10, 23, 35, 15,
    10, 42, 35, 15, 23, 15, 10, 15, 42, 35
]


# 1. Cardinalité
def calculer_cardinalite(donnees: list) -> int:
    return len(donnees)


# 2. Tuple des modalités
def calculer_modalites(donnees: list) -> tuple:
    return tuple(sorted(set(donnees)))


# 3. Tableau statistique (dictionnaire modalité: effectif)
def calculer_tableau_statistique(donnees: list) -> dict:
    modalites = calculer_modalites(donnees)
    return {mod: donnees.count(mod) for mod in modalites}


# 4. Affichage formaté
def afficher_tableau_statistique(tableau: dict) -> None:
    print(f"{'Modalité':>10} | {'Effectif':>10}")
    print("-" * 23)
    for mod, eff in tableau.items():
        print(f"{mod:>10} | {eff:>10}")
    print("-" * 23)
    print(f"{'Total':>10} | {sum(tableau.values()):>10}\n")


# 5. Mesures de tendance centrale
def calculer_moyenne(donnees: list) -> float:
    return sum(donnees) / len(donnees)


def calculer_mode(donnees: list) -> list:
    tableau = calculer_tableau_statistique(donnees)
    max_eff = max(tableau.values())
    return [mod for mod, eff in tableau.items() if eff == max_eff]


def calculer_mediane(donnees: list) -> float:
    triee = sorted(donnees)
    n = len(triee)
    milieu = n // 2
    if n % 2 == 1:
        return float(triee[milieu])
    return (triee[milieu - 1] + triee[milieu]) / 2


# 6. Mesures de dispersion
def calculer_etendue(donnees: list) -> float:
    return max(donnees) - min(donnees)


def calculer_ecart_absolu_total(donnees: list) -> float:
    moy = calculer_moyenne(donnees)
    return sum(abs(x - moy) for x in donnees)


def calculer_ecart_moyen(donnees: list) -> float:
    return calculer_ecart_absolu_total(donnees) / len(donnees)


def calculer_variance(donnees: list) -> float:
    moy = calculer_moyenne(donnees)
    return sum((x - moy) ** 2 for x in donnees) / len(donnees)


def calculer_ecart_type(donnees: list) -> float:
    return math.sqrt(calculer_variance(donnees))


def calculer_coefficient_variation(donnees: list) -> float:
    return calculer_ecart_type(donnees) / calculer_moyenne(donnees)


def calculer_quartiles(donnees: list) -> tuple[float, float]:
    triee = sorted(donnees)
    n = len(triee)
    
    # Méthode standard par rang n/4 et 3n/4
    idx_q1 = int(math.ceil(n / 4)) - 1
    idx_q3 = int(math.ceil(3 * n / 4)) - 1
    return triee[idx_q1], triee[idx_q3]


def calculer_ecart_interquartile(donnees: list) -> float:
    q1, q3 = calculer_quartiles(donnees)
    return q3 - q1


# 7. Diagramme en bâtons
def tracer_diagramme_batons(donnees: list) -> None:
    tableau = calculer_tableau_statistique(donnees)
    modalites = list(tableau.keys())
    effectifs = list(tableau.values())

    plt.figure()
    plt.bar(modalites, effectifs, width=0.01)
    plt.xlabel("Nombre de notifications")
    plt.ylabel("Effectif")
    plt.title("Diagramme en bâtons du nombre de notifications")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


# 8. Boîte à moustaches
def tracer_boite_moustaches(donnees: list) -> None:
    plt.figure()
    plt.boxplot(donnees)
    plt.ylabel("Nombre de notifications")
    plt.title("Boîte à moustaches de l'échantillon")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


# Exécution principale
if __name__ == "__main__":
    card = calculer_cardinalite(echantillon)
    mods = calculer_modalites(echantillon)
    tab = calculer_tableau_statistique(echantillon)

    print(f"Cardinalité : {card}")
    print(f"Modalités : {mods}\n")

    print("Tableau statistique :")
    afficher_tableau_statistique(tab)

    print("--- Mesures de tendance centrale ---")
    print(f"Moyenne : {calculer_moyenne(echantillon):.2f}")
    print(f"Mode(s) : {calculer_mode(echantillon)}")
    print(f"Médiane : {calculer_mediane(echantillon):.2f}\n")

    print("--- Mesures de dispersion ---")
    print(f"Étendue : {calculer_etendue(echantillon)}")
    print(f"Écart-absolu (somme) : {calculer_ecart_absolu_total(echantillon):.2f}")
    print(f"Écart moyen : {calculer_ecart_moyen(echantillon):.2f}")
    print(f"Variance : {calculer_variance(echantillon):.2f}")
    print(f"Écart-type : {calculer_ecart_type(echantillon):.2f}")
    print(f"Coefficient de variation : {calculer_coefficient_variation(echantillon):.4f}")
    q1, q3 = calculer_quartiles(echantillon)
    print(f"Q1 : {q1} | Q3 : {q3}")
    print(f"Écart interquartile (EIQ) : {calculer_ecart_interquartile(echantillon)}")

    # Tracé des graphiques
    tracer_diagramme_batons(echantillon)
    tracer_boite_moustaches(echantillon)